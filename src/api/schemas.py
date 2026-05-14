from pydantic import BaseModel, Field
from typing import List, Dict, Any


class ChatRequest(BaseModel):
    query: str = Field(..., min_length=2, examples=["What is RAG?"])


class ChatResponse(BaseModel):
    answer: str
    citations: List[Dict[str, Any]]
    debug_trace: List[str]


class IngestRequest(BaseModel):
    folder_path: str = "data/sample_docs"
