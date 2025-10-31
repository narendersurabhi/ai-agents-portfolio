from __future__ import annotations

import glob
import json
import os
from array import array
from typing import Any, Dict, List

try:  # optional
    import numpy as _np
except Exception:  # pragma: no cover
    _np = None  # type: ignore

try:  # optional
    import faiss  # type: ignore
except Exception:  # pragma: no cover
    faiss = None  # type: ignore

try:  # optional
    import chromadb
    from chromadb.config import Settings
except Exception:  # pragma: no cover
    chromadb = None  # type: ignore
    Settings = None  # type: ignore

try:  # optional
    from opensearchpy import OpenSearch  # type: ignore
except Exception:  # pragma: no cover
    OpenSearch = None  # type: ignore

try:  # optional
    import redis  # type: ignore
    from redis.commands.search.query import Query  # type: ignore
except Exception:  # pragma: no cover
    redis = None  # type: ignore
    Query = None  # type: ignore

from .embed import embed_text, cosine_similarity


class LocalVectorStore:
    """Vector search over document chunks with configurable backends."""

    def __init__(self, path: str):
        self.path = path
        self._meta: Dict[str, Any] = {}
        self._records: List[Dict[str, Any]] | None = None
        self._vectors = None
        self._faiss_index = None
        self._chroma_client = None
        self._chroma_collection = None
        self._opensearch_client = None
        self._redis_client = None

        self._load_meta()
        backend_override = os.getenv("VECTOR_BACKEND")
        meta_backend = self._meta.get("backend") if isinstance(self._meta, dict) else None
        self._backend = (backend_override or meta_backend or "json").lower()

        if self._backend == "numpy" and _np is None:
            raise RuntimeError("VECTOR_BACKEND=numpy requires the numpy package")
        if self._backend == "faiss" and faiss is None:
            raise RuntimeError("VECTOR_BACKEND=faiss requires the faiss-cpu package")
        if self._backend == "chroma" and chromadb is None:
            raise RuntimeError("VECTOR_BACKEND=chroma requires the chromadb package")
        if self._backend == "opensearch" and OpenSearch is None:
            raise RuntimeError("VECTOR_BACKEND=opensearch requires opensearch-py")
        if self._backend == "redis" and (redis is None or Query is None):
            raise RuntimeError("VECTOR_BACKEND=redis requires redis-py with RediSearch support")

        self._collection_name = (
            os.getenv("VECTOR_COLLECTION")
            or (self._meta.get("collection") if isinstance(self._meta, dict) else None)
            or "docs"
        )
        self._opensearch_url = os.getenv("OPENSEARCH_URL", "http://localhost:9200")
        self._opensearch_user = os.getenv("OPENSEARCH_USER") or None
        self._opensearch_password = os.getenv("OPENSEARCH_PASSWORD") or None
        self._opensearch_verify = os.getenv("OPENSEARCH_VERIFY", "true").lower() != "false"
        self._opensearch_index = (
            os.getenv("OPENSEARCH_INDEX")
            or (self._meta.get("opensearch_index") if isinstance(self._meta, dict) else None)
            or "docs-index"
        )
        self._redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
        self._redis_password = os.getenv("REDIS_PASSWORD") or None
        self._redis_index = (
            os.getenv("REDIS_INDEX")
            or (self._meta.get("redis_index") if isinstance(self._meta, dict) else None)
            or "docs-index"
        )
        self._redis_prefix = os.getenv("REDIS_PREFIX", "doc:")
        self._redis_vector_field = (
            os.getenv("REDIS_VECTOR_FIELD")
            or (self._meta.get("redis_vector_field") if isinstance(self._meta, dict) else None)
            or "embedding"
        )

    def search(
        self,
        query: str,
        top_k: int = 4,
        *,
        include_text: bool = True,
        include_embedding: bool = False,
    ) -> List[Dict[str, Any]]:
        self._ensure_records()
        query_vec = embed_text(query)

        if self._backend == "json":
            return self._json_search(query_vec, top_k, include_text, include_embedding)
        if self._backend == "numpy":
            return self._numpy_search(query_vec, top_k, include_text, include_embedding)
        if self._backend == "faiss":
            return self._faiss_search(query_vec, top_k, include_text, include_embedding)
        if self._backend == "chroma":
            return self._chroma_search(query_vec, top_k, include_text, include_embedding)
        if self._backend == "opensearch":
            return self._opensearch_search(query_vec, top_k, include_text, include_embedding)
        if self._backend == "redis":
            return self._redis_search(query_vec, top_k, include_text, include_embedding)
        raise ValueError(f"Unsupported vector backend: {self._backend}")

    def _json_search(
        self,
        query_vec: List[float],
        top_k: int,
        include_text: bool,
        include_embedding: bool,
    ) -> List[Dict[str, Any]]:
        if not self._records:
            return []
        scored: List[tuple[float, Dict[str, Any]]] = []
        for rec in self._records:
            sim = cosine_similarity(query_vec, rec.get("embedding", []))
            scored.append((sim, rec))
        scored.sort(key=lambda item: item[0], reverse=True)
        results: List[Dict[str, Any]] = []
        for sim, rec in scored[:top_k]:
            item = {
                "id": rec.get("id"),
                "score": float(sim),
                "chunk": int(rec.get("chunk", 0)),
            }
            if include_text:
                item["text"] = rec.get("text", "")
            if include_embedding:
                item["embedding"] = rec.get("embedding", [])
            results.append(item)
        return results

    def _numpy_search(
        self,
        query_vec: List[float],
        top_k: int,
        include_text: bool,
        include_embedding: bool,
    ) -> List[Dict[str, Any]]:
        if _np is None:
            raise RuntimeError("NumPy backend not available")
        self._ensure_numpy_vectors()
        if self._vectors is None:
            raise RuntimeError("NumPy vectors file not found")
        query_arr = _np.array(query_vec, dtype="float32")
        if query_arr.ndim != 1:
            query_arr = query_arr.reshape(-1)
        denom = _np.linalg.norm(query_arr)
        if denom == 0:
            scores = _np.zeros(len(self._vectors), dtype="float32")
        else:
            scores = self._vectors.dot(query_arr / denom)
        top_idx = _np.argsort(scores)[::-1][:top_k]
        results: List[Dict[str, Any]] = []
        for idx in top_idx:
            rec = self._records[idx]
            item: Dict[str, Any] = {
                "id": rec.get("id"),
                "score": float(scores[idx]),
                "chunk": int(rec.get("chunk", 0)),
            }
            if include_text:
                item["text"] = rec.get("text", "")
            if include_embedding:
                item["embedding"] = rec.get("embedding", [])
            results.append(item)
        return results

    def _faiss_search(
        self,
        query_vec: List[float],
        top_k: int,
        include_text: bool,
        include_embedding: bool,
    ) -> List[Dict[str, Any]]:
        if faiss is None or _np is None:
            raise RuntimeError("Faiss backend not available")
        self._ensure_faiss_index()
        if self._faiss_index is None:
            raise RuntimeError("Faiss index missing")
        query_arr = _np.array(query_vec, dtype="float32")
        if query_arr.ndim != 1:
            query_arr = query_arr.reshape(-1)
        faiss.normalize_L2(query_arr.reshape(1, -1))
        distances, indices = self._faiss_index.search(query_arr.reshape(1, -1), top_k)
        results: List[Dict[str, Any]] = []
        for score, idx in zip(distances[0], indices[0]):
            if idx < 0 or idx >= len(self._records):
                continue
            rec = self._records[idx]
            item: Dict[str, Any] = {
                "id": rec.get("id"),
                "score": float(score),
                "chunk": int(rec.get("chunk", 0)),
            }
            if include_text:
                item["text"] = rec.get("text", "")
            if include_embedding:
                item["embedding"] = rec.get("embedding", [])
            results.append(item)
        return results

    def _chroma_search(
        self,
        query_vec: List[float],
        top_k: int,
        include_text: bool,
        include_embedding: bool,
    ) -> List[Dict[str, Any]]:
        self._ensure_chroma_collection()
        if self._chroma_collection is None:
            raise RuntimeError("Chroma backend not initialized")
        include = ["metadatas", "documents", "distances"]
        if include_embedding:
            include.append("embeddings")
        response = self._chroma_collection.query(
            query_embeddings=[query_vec],
            n_results=top_k,
            include=include,
        )
        ids = response.get("ids", [[]])
        documents = response.get("documents", [[]])
        metadatas = response.get("metadatas", [[]])
        distances = response.get("distances", [[]])
        embeddings = response.get("embeddings", [[]]) if include_embedding else [[]]
        if include_embedding and _np is not None and isinstance(embeddings, _np.ndarray):
            embeddings = embeddings.tolist()
        results: List[Dict[str, Any]] = []
        for idx, identifier in enumerate(ids[0] if ids else []):
            metadata: Dict[str, Any] = metadatas[0][idx] if metadatas and metadatas[0] else {}
            dist_list = distances[0] if distances else []
            dist_val = dist_list[idx] if idx < len(dist_list) else None
            score = 1.0 - float(dist_val) if dist_val is not None else 0.0
            item: Dict[str, Any] = {
                "id": metadata.get("id") or identifier,
                "score": score,
                "chunk": int(metadata.get("chunk", 0)),
            }
            if include_text:
                item["text"] = documents[0][idx] if documents and documents[0] else ""
            if include_embedding and embeddings:
                batch = embeddings[0]
                if isinstance(batch, list) and idx < len(batch):
                    item["embedding"] = batch[idx]
                else:
                    item["embedding"] = []
            results.append(item)
        return results

    def _opensearch_search(
        self,
        query_vec: List[float],
        top_k: int,
        include_text: bool,
        include_embedding: bool,
    ) -> List[Dict[str, Any]]:
        self._ensure_opensearch_client()
        if self._opensearch_client is None:
            raise RuntimeError("OpenSearch backend not initialized")
        body = {
            "size": top_k,
            "query": {"knn": {"embedding": {"vector": query_vec, "k": top_k}}},
        }
        response = self._opensearch_client.search(index=self._opensearch_index, body=body)
        hits = response.get("hits", {}).get("hits", [])
        results: List[Dict[str, Any]] = []
        for hit in hits:
            source = hit.get("_source", {})
            item: Dict[str, Any] = {
                "id": source.get("document_id") or hit.get("_id"),
                "score": float(hit.get("_score", 0.0)),
                "chunk": int(source.get("chunk", 0)),
            }
            if include_text:
                item["text"] = source.get("text", "")
            if include_embedding:
                item["embedding"] = source.get("embedding", [])
            results.append(item)
        return results

    def _redis_search(
        self,
        query_vec: List[float],
        top_k: int,
        include_text: bool,
        include_embedding: bool,
    ) -> List[Dict[str, Any]]:
        self._ensure_redis_client()
        if self._redis_client is None or Query is None:
            raise RuntimeError("Redis backend not initialized")
        search = self._redis_client.ft(self._redis_index)
        vector_bytes = array("f", query_vec).tobytes()
        query = (
            Query(f"*=>[KNN {top_k} @{self._redis_vector_field}  AS vector_distance]")
            .sort_by("vector_distance")
            .return_fields("document_id", "chunk", "text", "vector_distance")
            .dialect(2)
        )
        response = search.search(query, query_params={"vec": vector_bytes})
        results: List[Dict[str, Any]] = []
        for doc in getattr(response, "docs", []):
            key = getattr(doc, "id", "")
            doc_id = getattr(doc, "document_id", None) or key
            chunk_val = getattr(doc, "chunk", 0)
            text_val = getattr(doc, "text", "")
            distance = float(getattr(doc, "vector_distance", 0.0))
            score = 1.0 - distance
            key_str = key.decode("utf-8", "ignore") if isinstance(key, bytes) else key
            item: Dict[str, Any] = {
                "id": doc_id.decode("utf-8", "ignore") if isinstance(doc_id, bytes) else doc_id,
                "score": score,
                "chunk": int(chunk_val),
            }
            if include_text:
                item["text"] = (
                    text_val.decode("utf-8", "ignore") if isinstance(text_val, bytes) else text_val
                )
            if include_embedding and key_str:
                raw = self._redis_client.hget(key_str, self._redis_vector_field)
                if raw:
                    arr = array("f")
                    arr.frombytes(raw)
                    item["embedding"] = list(arr)
                else:
                    item["embedding"] = []
            results.append(item)
        return results

    # ------------------------------------------------------------------
    def _load_meta(self) -> None:
        meta_path = os.path.join(self.path, "meta.json")
        try:
            with open(meta_path, "r", encoding="utf-8") as fh:
                self._meta = json.load(fh)
        except FileNotFoundError:
            self._meta = {}

    def _ensure_records(self) -> None:
        if self._records is not None:
            return
        idx_path = os.path.join(self.path, "index.jsonl")
        recs: List[Dict[str, Any]] = []
        try:
            with open(idx_path, "r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    obj = json.loads(line)
                    if isinstance(obj.get("embedding"), list):
                        recs.append(obj)
        except FileNotFoundError:
            recs = []
        self._records = recs

    def _ensure_numpy_vectors(self) -> None:
        if self._vectors is not None or _np is None:
            return
        vectors_path = os.path.join(self.path, "vectors.npy")
        if not os.path.exists(vectors_path):
            raise RuntimeError("vectors.npy not found for numpy backend")
        vectors = _np.load(vectors_path)
        if self._records is None or len(vectors) != len(self._records):
            raise RuntimeError("numpy vectors count does not match records")
        self._vectors = vectors

    def _ensure_faiss_index(self) -> None:
        if self._faiss_index is not None or faiss is None:
            return
        index_path = os.path.join(self.path, "faiss.index")
        if not os.path.exists(index_path):
            raise RuntimeError("faiss index file not found")
        try:
            index = faiss.read_index(index_path)
        except Exception as exc:
            raise RuntimeError(f"failed to read faiss index: {exc}") from exc
        if self._records is None or index.ntotal != len(self._records):
            raise RuntimeError("faiss index count does not match records")
        self._faiss_index = index

    def _ensure_chroma_collection(self) -> None:
        if self._backend != "chroma" or self._chroma_collection is not None:
            return
        if chromadb is None:
            raise RuntimeError("Chroma backend not available")
        try:
            settings = Settings(anonymized_telemetry=False) if Settings is not None else None
        except Exception:
            settings = None
        try:
            client = (
                chromadb.PersistentClient(path=self.path, settings=settings)
                if settings is not None
                else chromadb.PersistentClient(path=self.path)
            )
        except TypeError:
            client = chromadb.PersistentClient(path=self.path)
        except Exception as exc:
            raise RuntimeError(f"Failed to initialize Chroma client: {exc}") from exc
        try:
            collection = client.get_collection(self._collection_name)
        except Exception:
            collection = client.get_or_create_collection(
                self._collection_name,
                metadata={"hnsw:space": "cosine"},
            )
        self._chroma_client = client
        self._chroma_collection = collection

    def _ensure_opensearch_client(self) -> None:
        if self._backend != "opensearch" or self._opensearch_client is not None:
            return
        if OpenSearch is None:
            raise RuntimeError("OpenSearch backend not available")
        kwargs: Dict[str, Any] = {"hosts": [self._opensearch_url], "verify_certs": self._opensearch_verify}
        if self._opensearch_user:
            kwargs["http_auth"] = (self._opensearch_user, self._opensearch_password or "")
        try:
            self._opensearch_client = OpenSearch(**kwargs)
        except Exception as exc:
            raise RuntimeError(f"Failed to connect to OpenSearch: {exc}") from exc

    def _ensure_redis_client(self) -> None:
        if self._backend != "redis" or self._redis_client is not None:
            return
        if redis is None:
            raise RuntimeError("Redis backend not available")
        try:
            self._redis_client = redis.Redis.from_url(
                self._redis_url,
                password=self._redis_password,
                decode_responses=False,
            )
        except Exception as exc:
            raise RuntimeError(f"Failed to connect to Redis: {exc}") from exc
