from src.rag.ingestion import ingest_folder
from src.rag.vector_store import LocalVectorStore


if __name__ == "__main__":
    count = ingest_folder("data/sample_docs", LocalVectorStore())
    print(f"Ingested {count} chunks into local vector store")
