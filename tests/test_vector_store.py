from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from src.tools.vector_store import LocalVectorStore


def _write_index(path: Path, records: list[dict[str, object]]) -> None:
    with (path / "index.jsonl").open("w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec) + "\n")


def test_numpy_backend_rankings(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    index_dir = tmp_path / "numpy_idx"
    index_dir.mkdir()
    records = [
        {"id": "doc1", "chunk": 0, "text": "alpha", "embedding": [1.0, 0.0]},
        {"id": "doc2", "chunk": 1, "text": "beta", "embedding": [0.0, 1.0]},
    ]
    _write_index(index_dir, records)

    vectors = np.array([r["embedding"] for r in records], dtype="float32")
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    np.save(index_dir / "vectors.npy", vectors / norms)

    monkeypatch.setenv("VECTOR_BACKEND", "numpy")
    monkeypatch.setattr("src.tools.vector_store.embed_text", lambda _: [1.0, 0.0])

    store = LocalVectorStore(str(index_dir))
    results = store.search("alpha", top_k=2)

    assert [res["id"] for res in results] == ["doc1", "doc2"]


def test_numpy_missing_vectors(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    index_dir = tmp_path / "numpy_missing"
    index_dir.mkdir()
    records = [
        {"id": "docA", "chunk": 0, "text": "one", "embedding": [1.0, 0.0]},
    ]
    _write_index(index_dir, records)

    monkeypatch.setenv("VECTOR_BACKEND", "numpy")
    monkeypatch.setattr("src.tools.vector_store.embed_text", lambda _: [1.0, 0.0])

    store = LocalVectorStore(str(index_dir))
    with pytest.raises(RuntimeError):
        store.search("one", top_k=1)


def test_faiss_backend(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    faiss = pytest.importorskip("faiss")
    index_dir = tmp_path / "faiss_idx"
    index_dir.mkdir()
    records = [
        {"id": "doc1", "chunk": 0, "text": "alpha", "embedding": [1.0, 0.0]},
        {"id": "doc2", "chunk": 1, "text": "beta", "embedding": [0.0, 1.0]},
    ]
    _write_index(index_dir, records)

    vectors = np.array([r["embedding"] for r in records], dtype="float32")
    faiss.normalize_L2(vectors)
    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)
    faiss.write_index(index, str(index_dir / "faiss.index"))

    (index_dir / "meta.json").write_text(json.dumps({"backend": "faiss"}), encoding="utf-8")

    monkeypatch.setenv("VECTOR_BACKEND", "faiss")
    monkeypatch.setattr("src.tools.vector_store.embed_text", lambda _: [1.0, 0.0])

    store = LocalVectorStore(str(index_dir))
    results = store.search("alpha", top_k=2)

    assert results and results[0]["id"] == "doc1"




def test_faiss_reload(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    faiss = pytest.importorskip('faiss')
    index_dir = tmp_path / 'faiss_reload'
    index_dir.mkdir()
    records = [
        {'id': 'doc1', 'chunk': 0, 'text': 'alpha', 'embedding': [1.0, 0.0]},
        {'id': 'doc2', 'chunk': 1, 'text': 'beta', 'embedding': [0.0, 1.0]},
    ]
    _write_index(index_dir, records)

    vectors = np.array([r['embedding'] for r in records], dtype='float32')
    faiss.normalize_L2(vectors)
    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)
    local_path = index_dir / 'faiss.index'
    faiss.write_index(index, str(local_path))
    (index_dir / 'meta.json').write_text(json.dumps({'backend': 'faiss'}), encoding='utf-8')

    monkeypatch.setenv('VECTOR_BACKEND', 'faiss')
    monkeypatch.setenv('FAISS_LOCAL_PATH', str(local_path))
    for env in ('FAISS_S3_BUCKET', 'FAISS_S3_KEY'):
        monkeypatch.delenv(env, raising=False)
    monkeypatch.setattr('src.tools.vector_store.embed_text', lambda _: [1.0, 0.0])

    store = LocalVectorStore(str(index_dir))
    initial = store.search('alpha', top_k=2)
    assert initial and initial[0]['id'] == 'doc1'

    # Write a new index where doc2 is the closest match
    new_vectors = np.array([[0.0, 1.0], [1.0, 0.0]], dtype='float32')
    faiss.normalize_L2(new_vectors)
    new_index = faiss.IndexFlatIP(new_vectors.shape[1])
    new_index.add(new_vectors)
    faiss.write_index(new_index, str(local_path))

    store.reload()
    refreshed = store.search('alpha', top_k=2)
    assert refreshed and refreshed[0]['id'] == 'doc2'
def test_chroma_backend(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    chroma = pytest.importorskip("chromadb")
    try:
        from chromadb.config import Settings
    except Exception:
        Settings = None  # type: ignore

    index_dir = tmp_path / "chroma_idx"
    index_dir.mkdir()
    records = [
        {"id": "doc1", "chunk": 0, "text": "alpha details", "embedding": [1.0, 0.0]},
        {"id": "doc2", "chunk": 1, "text": "beta info", "embedding": [0.0, 1.0]},
    ]
    _write_index(index_dir, records)
    (index_dir / "meta.json").write_text(
        json.dumps({"backend": "chroma", "collection": "unit_test"}), encoding="utf-8"
    )

    if Settings is not None:
        try:
            settings = Settings(anonymized_telemetry=False)
        except Exception:
            settings = None
    else:
        settings = None

    if settings is not None:
        client = chroma.PersistentClient(path=str(index_dir), settings=settings)
    else:
        client = chroma.PersistentClient(path=str(index_dir))
    try:
        client.delete_collection("unit_test")
    except Exception:
        pass
    collection = client.create_collection("unit_test", metadata={"hnsw:space": "cosine"})
    collection.add(
        ids=["doc1::0", "doc2::1"],
        embeddings=[[1.0, 0.0], [0.0, 1.0]],
        documents=["alpha details", "beta info"],
        metadatas=[{"id": "doc1", "chunk": 0}, {"id": "doc2", "chunk": 1}],
    )

    monkeypatch.setenv("VECTOR_BACKEND", "chroma")
    monkeypatch.setenv("VECTOR_COLLECTION", "unit_test")
    monkeypatch.setattr("src.tools.vector_store.embed_text", lambda _: [1.0, 0.0])

    store = LocalVectorStore(str(index_dir))
    results = store.search("alpha", top_k=1)
    assert results and results[0]["id"] == "doc1"


def test_opensearch_backend_missing_client(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    index_dir = tmp_path / "opensearch_idx"
    index_dir.mkdir()
    records = [{"id": "doc1", "chunk": 0, "text": "alpha", "embedding": [1.0, 0.0]}]
    _write_index(index_dir, records)
    (index_dir / "meta.json").write_text(json.dumps({"backend": "opensearch"}), encoding="utf-8")

    monkeypatch.setenv("VECTOR_BACKEND", "opensearch")
    monkeypatch.setattr("src.tools.vector_store.OpenSearch", None)

    with pytest.raises(RuntimeError):
        LocalVectorStore(str(index_dir))


def test_redis_backend_missing_client(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    index_dir = tmp_path / "redis_idx"
    index_dir.mkdir()
    records = [{"id": "docA", "chunk": 0, "text": "one", "embedding": [1.0, 0.0]}]
    _write_index(index_dir, records)
    (index_dir / "meta.json").write_text(json.dumps({"backend": "redis"}), encoding="utf-8")

    monkeypatch.setenv("VECTOR_BACKEND", "redis")
    monkeypatch.setattr("src.tools.vector_store.redis", None)

    with pytest.raises(RuntimeError):
        LocalVectorStore(str(index_dir))
