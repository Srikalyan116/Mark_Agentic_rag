from fastapi import FastAPI, HTTPException

from src.agents.graph import AgentGraph
from src.api.schemas import ChatRequest, ChatResponse, IngestRequest
from src.config.settings import settings
from src.rag.ingestion import ingest_folder
from src.rag.vector_store import LocalVectorStore

app = FastAPI(title=settings.app_name, version="1.0.0")
agent = AgentGraph()


@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}


@app.post("/ingest")
def ingest(request: IngestRequest):
    try:
        count = ingest_folder(request.folder_path, LocalVectorStore())
        return {"status": "success", "chunks_ingested": count}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    state = agent.run(request.query)
    citations = [
        {
            "source": doc.get("source"),
            "chunk_id": doc.get("chunk_id"),
            "score": round(doc.get("score", 0), 4),
        }
        for doc in state.get("retrieved_docs", [])
    ]
    return ChatResponse(
        answer=state["answer"],
        citations=citations,
        debug_trace=state.get("debug_trace", []),
    )
