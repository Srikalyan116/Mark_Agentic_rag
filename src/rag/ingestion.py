from pathlib import Path
from typing import List, Dict

from src.rag.chunker import chunk_text
from src.rag.vector_store import LocalVectorStore


def ingest_folder(folder_path: str, store: LocalVectorStore) -> int:
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    docs: List[Dict] = []
    for path in folder.glob("*.txt"):
        text = path.read_text(encoding="utf-8")
        chunks = chunk_text(text)
        for idx, chunk in enumerate(chunks):
            docs.append(
                {
                    "source": path.name,
                    "chunk_id": idx,
                    "text": chunk,
                }
            )

    if docs:
        store.add_documents(docs)
    return len(docs)
