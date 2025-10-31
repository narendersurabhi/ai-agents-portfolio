import argparse
import json
import os
import pathlib
import sys
from array import array
from typing import List, Tuple

from src.tools.embed import embed_texts


def _read_text_from_file(path: pathlib.Path) -> str:
    suf = path.suffix.lower()
    if suf in {".txt", ".md", ".markdown"}:
        return path.read_text(encoding="utf-8", errors="ignore")
    if suf == ".pdf":
        try:
            from pypdf import PdfReader  # type: ignore
        except Exception:
            print(f"warn: skipping PDF (pypdf not installed): {path}", file=sys.stderr)
            return ""
        try:
            reader = PdfReader(str(path))
            texts = []
            for page in reader.pages:
                try:
                    texts.append(page.extract_text() or "")
                except Exception:
                    continue
            return "\n".join(texts)
        except Exception as exc:
            print(f"warn: failed to read PDF {path}: {exc}", file=sys.stderr)
            return ""
    return ""


def _chunk_text(text: str, chunk_size: int = 1200, overlap: int = 150) -> List[str]:
    if not text:
        return []
    chunks: List[str] = []
    start = 0
    n = len(text)
    while start < n:
        end = min(n, start + chunk_size)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end == n:
            break
        start = max(0, end - overlap)
    return chunks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", type=pathlib.Path, required=True, help="Source docs directory")
    parser.add_argument("--out", type=pathlib.Path, required=True, help="Output index directory")
    parser.add_argument("--chunk-size", type=int, default=1200, help="Chunk size in characters")
    parser.add_argument("--overlap", type=int, default=150, help="Overlap between chunks in characters")
    parser.add_argument(
        "--backend",
        choices=["json", "numpy", "faiss", "chroma", "opensearch", "redis"],
        default=os.getenv("VECTOR_BACKEND", "json"),
        help="Vector index backend to materialize",
    )
    args = parser.parse_args()

    src: pathlib.Path = args.src
    out: pathlib.Path = args.out
    chunk_size: int = args.chunk_size
    overlap: int = args.overlap
    backend: str = args.backend.lower()
    collection_name = os.getenv("VECTOR_COLLECTION", "docs")

    if not src.exists():
        print(f"error: source does not exist: {src}", file=sys.stderr)
        return 2
    if not src.is_dir():
        print(f"error: source is not a directory: {src}", file=sys.stderr)
        return 2

    out.mkdir(parents=True, exist_ok=True)

    files: List[pathlib.Path] = []
    for suffix in ("*.txt", "*.md", "*.markdown", "*.pdf"):
        files.extend(src.glob(suffix))
    if not files:
        print(f"warn: no supported docs in {src}", file=sys.stderr)

    records: List[Tuple[str, int, str]] = []
    for fp in files:
        text = _read_text_from_file(fp)
        if not text:
            continue
        chunks = _chunk_text(text, chunk_size=chunk_size, overlap=overlap)
        for idx, chunk in enumerate(chunks):
            records.append((str(fp), idx, chunk))

    texts = [r[2] for r in records]
    embeddings: List[List[float]] = []
    batch = 64
    for i in range(0, len(texts), batch):
        embeddings.extend(embed_texts(texts[i : i + batch]))

    idx_path = out / "index.jsonl"
    with idx_path.open("w", encoding="utf-8") as fh:
        for (doc_id, chunk_idx, chunk_text), embedding in zip(records, embeddings):
            fh.write(
                json.dumps(
                    {
                        "id": doc_id,
                        "chunk": chunk_idx,
                        "text": chunk_text,
                        "embedding": embedding,
                    }
                )
                + "\n"
            )

    opensearch_meta: dict[str, str] = {}
    redis_meta: dict[str, str] = {}

    if backend == "json":
        effective_backend = "json"

    elif backend == "numpy":
        try:
            import numpy as np
        except Exception as exc:
            raise RuntimeError(f"numpy backend unavailable: {exc}") from exc
        if not embeddings:
            raise RuntimeError("numpy backend requires embeddings; none were generated")
        vector_array = np.array(embeddings, dtype="float32")
        if vector_array.ndim != 2 or vector_array.shape[1] == 0:
            raise RuntimeError("numpy backend requires 2D embeddings array")
        norms = np.linalg.norm(vector_array, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        vector_array = vector_array / norms
        np.save(out / "vectors.npy", vector_array)
        effective_backend = "numpy"

    elif backend == "faiss":
        try:
            import faiss  # type: ignore
            import numpy as np
        except Exception as exc:
            raise RuntimeError(f"faiss backend unavailable: {exc}") from exc
        if not embeddings:
            raise RuntimeError("faiss backend requires embeddings; none were generated")
        vector_array = np.array(embeddings, dtype="float32")
        if vector_array.ndim != 2 or vector_array.shape[1] == 0:
            raise RuntimeError("faiss backend requires 2D embeddings array")
        faiss.normalize_L2(vector_array)
        index = faiss.IndexFlatIP(vector_array.shape[1])
        index.add(vector_array)
        faiss.write_index(index, str(out / "faiss.index"))
        effective_backend = "faiss"

    elif backend == "chroma":
        try:
            import chromadb
            from chromadb.config import Settings
        except Exception as exc:
            raise RuntimeError(f"chroma backend unavailable: {exc}") from exc
        try:
            settings = Settings(anonymized_telemetry=False)
        except Exception:
            settings = None
        try:
            client = (
                chromadb.PersistentClient(path=str(out), settings=settings)
                if settings is not None
                else chromadb.PersistentClient(path=str(out))
            )
        except TypeError:
            client = chromadb.PersistentClient(path=str(out))
        except Exception as exc:
            raise RuntimeError(f"failed to initialize Chroma client: {exc}") from exc

        try:
            client.delete_collection(collection_name)
        except Exception:
            pass
        collection = client.get_or_create_collection(
            collection_name,
            metadata={"hnsw:space": "cosine"},
        )
        if records and embeddings:
            batch_size = 64
            for i in range(0, len(records), batch_size):
                rec_batch = records[i : i + batch_size]
                emb_batch = embeddings[i : i + batch_size]
                ids = [f"{doc_id}::{chunk_idx}" for doc_id, chunk_idx, _ in rec_batch]
                documents = [text for _, _, text in rec_batch]
                metadatas = [{"id": doc_id, "chunk": chunk_idx} for doc_id, chunk_idx, _ in rec_batch]
                collection.add(ids=ids, embeddings=emb_batch, documents=documents, metadatas=metadatas)
        effective_backend = "chroma"

    elif backend == "opensearch":
        try:
            from opensearchpy import OpenSearch, helpers  # type: ignore
        except Exception as exc:
            raise RuntimeError(f"opensearch backend unavailable: {exc}") from exc
        if not embeddings:
            raise RuntimeError("opensearch backend requires embeddings; none were generated")

        dimension = len(embeddings[0])
        url = os.getenv("OPENSEARCH_URL", "http://localhost:9200")
        user = os.getenv("OPENSEARCH_USER")
        password = os.getenv("OPENSEARCH_PASSWORD")
        verify = os.getenv("OPENSEARCH_VERIFY", "true").lower() != "false"
        index_name = os.getenv("OPENSEARCH_INDEX", "docs-index")

        kwargs: dict[str, object] = {"hosts": [url], "verify_certs": verify}
        if user:
            kwargs["http_auth"] = (user, password or "")
        try:
            client = OpenSearch(**kwargs)
        except Exception as exc:
            raise RuntimeError(f"failed to connect to OpenSearch: {exc}") from exc

        mapping = {
            "settings": {"index": {"knn": True}},
            "mappings": {
                "properties": {
                    "embedding": {
                        "type": "knn_vector",
                        "dimension": dimension,
                        "method": {
                            "name": "hnsw",
                            "space_type": "cosinesimil",
                            "engine": "nmslib",
                            "parameters": {"ef_construction": 128, "m": 16},
                        },
                    },
                    "document_id": {"type": "keyword"},
                    "chunk": {"type": "integer"},
                    "text": {"type": "text"},
                }
            },
        }
        try:
            if not client.indices.exists(index=index_name):
                client.indices.create(index=index_name, body=mapping)
        except Exception as exc:
            raise RuntimeError(f"failed to ensure OpenSearch index: {exc}") from exc

        actions = []
        for (doc_id, chunk_idx, ch_text), embedding in zip(records, embeddings):
            actions.append(
                {
                    "_op_type": "index",
                    "_index": index_name,
                    "_id": f"{doc_id}::{chunk_idx}",
                    "_source": {
                        "document_id": doc_id,
                        "chunk": chunk_idx,
                        "text": ch_text,
                        "embedding": embedding,
                    },
                }
            )
        try:
            if actions:
                helpers.bulk(client, actions, refresh=True)
        except Exception as exc:
            raise RuntimeError(f"failed to bulk index OpenSearch data: {exc}") from exc

        effective_backend = "opensearch"
        opensearch_meta = {"opensearch_index": index_name}

    elif backend == "redis":
        try:
            import redis  # type: ignore
            from redis.commands.search.field import NumericField, TextField, VectorField  # type: ignore
            from redis.commands.search.indexDefinition import IndexDefinition, IndexType  # type: ignore
        except Exception as exc:
            raise RuntimeError(f"redis backend unavailable: {exc}") from exc
        if not embeddings:
            raise RuntimeError("redis backend requires embeddings; none were generated")

        url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
        password = os.getenv("REDIS_PASSWORD")
        index_name = os.getenv("REDIS_INDEX", "docs-index")
        prefix = os.getenv("REDIS_PREFIX", "doc:")
        vector_field = os.getenv("REDIS_VECTOR_FIELD", "embedding")
        dimension = len(embeddings[0])

        try:
            client = redis.Redis.from_url(url, password=password, decode_responses=False)
            ft = client.ft(index_name)
            try:
                ft.info()
            except Exception:
                schema = (
                    TextField("document_id"),
                    NumericField("chunk"),
                    TextField("text"),
                    VectorField(
                        vector_field,
                        "HNSW",
                        {
                            "TYPE": "FLOAT32",
                            "DIM": dimension,
                            "DISTANCE_METRIC": "COSINE",
                            "INITIAL_CAP": max(len(embeddings), 1000),
                            "M": 16,
                            "EF_CONSTRUCTION": 200,
                        },
                    ),
                )
                definition = IndexDefinition(prefix=[prefix], index_type=IndexType.HASH)
                ft.create_index(schema, definition=definition)
            pipe = client.pipeline(transaction=False)
            for (doc_id, chunk_idx, ch_text), embedding in zip(records, embeddings):
                key = f"{prefix}{doc_id}::{chunk_idx}"
                data = {
                    "document_id": doc_id,
                    "chunk": chunk_idx,
                    "text": ch_text,
                    vector_field: array("f", embedding).tobytes(),
                }
                pipe.hset(key, mapping=data)
            pipe.execute()
        except Exception as exc:
            raise RuntimeError(f"failed to write to Redis: {exc}") from exc

        effective_backend = "redis"
        redis_meta = {
            "redis_index": index_name,
            "redis_prefix": prefix,
            "redis_vector_field": vector_field,
        }

    else:
        raise ValueError(f"Unsupported backend: {backend}")

    meta = {"built": True, "chunks": len(records), "backend": effective_backend}
    if effective_backend == "chroma":
        meta["collection"] = collection_name
    if opensearch_meta:
        meta.update(opensearch_meta)
    if redis_meta:
        meta.update(redis_meta)
    (out / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    print(f"Indexed {len(records)} chunks from {len(files)} files into {out} ({effective_backend} backend)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
