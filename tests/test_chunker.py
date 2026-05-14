from src.rag.chunker import chunk_text


def test_chunk_text_returns_chunks():
    chunks = chunk_text("hello world " * 100, chunk_size=100, overlap=10)
    assert len(chunks) > 1
    assert all(isinstance(chunk, str) for chunk in chunks)
