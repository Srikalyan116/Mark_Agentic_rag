import pickle
from pathlib import Path
from typing import List, Dict, Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class LocalVectorStore:
    """Simple local vector store using TF-IDF for demo and interview purposes."""

    def __init__(self, path: str = ".vector_store.pkl"):
        self.path = Path(path)
        self.documents: List[Dict[str, Any]] = []
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = None

    def add_documents(self, docs: List[Dict[str, Any]]) -> None:
        self.documents.extend(docs)
        texts = [doc["text"] for doc in self.documents]
        self.matrix = self.vectorizer.fit_transform(texts)
        self.save()

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        if not self.documents or self.matrix is None:
            self.load()

        if not self.documents or self.matrix is None:
            return []

        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.matrix).flatten()
        ranked_indices = scores.argsort()[::-1][:top_k]

        results = []
        for idx in ranked_indices:
            doc = dict(self.documents[idx])
            doc["score"] = float(scores[idx])
            results.append(doc)
        return results

    def save(self) -> None:
        with self.path.open("wb") as file:
            pickle.dump(
                {
                    "documents": self.documents,
                    "vectorizer": self.vectorizer,
                    "matrix": self.matrix,
                },
                file,
            )

    def load(self) -> None:
        if not self.path.exists():
            return
        with self.path.open("rb") as file:
            payload = pickle.load(file)
        self.documents = payload["documents"]
        self.vectorizer = payload["vectorizer"]
        self.matrix = payload["matrix"]
