# Agentic RAG Assistant — Professional AI/ML + LLM Engineering Project

A production-style AI application demonstrating Python, FastAPI, RAG, vector search, prompt engineering, tool use, agent workflows, debugging, and LLM API integration.



This repo maps directly to AI/ML Engineer and LLM Application Engineer job requirements:

- Python software engineering
- LLM API integration with OpenAI/Azure/Open-source compatible APIs
- RAG architecture using embeddings + vector store
- Agent workflow using LangGraph-style state transitions
- Tool-use pattern for calculator, document search, and web-safe mock tools
- Prompt engineering with structured outputs
- Failure handling, retries, logging, and debug traces
- FastAPI production backend
- Unit tests, Docker, CI pipeline, and clean GitHub documentation

## Architecture

```text
User Query
   ↓
FastAPI /chat endpoint
   ↓
Agent Graph
   ├── classify intent
   ├── retrieve context from vector store
   ├── call tools when needed
   ├── generate grounded answer
   └── return answer + citations + debug trace
```

## Features

- `/health` API for readiness checks
- `/ingest` API to ingest documents
- `/chat` API to ask questions
- Local TF-IDF vector search fallback, no paid API required
- Optional OpenAI/Azure OpenAI integration
- Agent state machine inspired by LangGraph
- Prompt templates separated from business logic
- Tool registry for extensible tools
- Tests with pytest
- Docker and GitHub Actions included

## Tech Stack

- Python 3.10+
- FastAPI
- Pydantic
- scikit-learn
- LangChain-ready structure
- LangGraph-style custom graph implementation
- Uvicorn
- Pytest
- Docker

## Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/agentic-rag-assistant.git
cd agentic-rag-assistant
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts_ingest_sample.py
uvicorn src.api.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Example API Request

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query":"Explain what RAG is and why vector databases are useful"}'
```

## Environment Variables

Copy `.env.example` to `.env`.

```bash
cp .env.example .env
```

Optional variables:

```env
LLM_PROVIDER=local
OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Project Structure

```text
agentic-rag-assistant/
├── src/
│   ├── api/              # FastAPI routes
│   ├── agents/           # Agent graph and state logic
│   ├── rag/              # Retriever, chunking, vector store
│   ├── tools/            # Tool registry and tool functions
│   ├── config/           # Settings
│   └── utils/            # Logging and helpers
├── data/sample_docs/     # Example knowledge documents
├── tests/                # Unit tests
├── .github/workflows/    # CI pipeline
├── Dockerfile
├── docker-compose.yml
└── README.md
```

