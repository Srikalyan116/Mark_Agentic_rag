from typing import List


def chunk_text(text: str, chunk_size: int = 600, overlap: int = 80) -> List[str]:
    """Split long text into overlapping chunks."""
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")

    clean = " ".join(text.split())
    chunks = []
    start = 0

    while start < len(clean):
        end = start + chunk_size
        chunk = clean[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end - overlap

    return chunks
