from typing import TypedDict, List, Dict, Any

from src.agents.llm_client import LLMClient
from src.agents.prompts import ANSWER_TEMPLATE
from src.rag.vector_store import LocalVectorStore
from src.tools.basic_tools import build_default_registry


class AgentState(TypedDict, total=False):
    query: str
    intent: str
    retrieved_docs: List[Dict[str, Any]]
    tool_name: str | None
    tool_output: str
    answer: str
    debug_trace: List[str]


class AgentGraph:
    """LangGraph-style workflow implemented without external dependency."""

    def __init__(self):
        self.store = LocalVectorStore()
        self.llm = LLMClient()
        self.tools = build_default_registry()

    def run(self, query: str) -> AgentState:
        state: AgentState = {"query": query, "debug_trace": []}
        state = self.classify_intent(state)
        state = self.retrieve_context(state)
        state = self.maybe_use_tool(state)
        state = self.generate_answer(state)
        return state

    def classify_intent(self, state: AgentState) -> AgentState:
        query = state["query"].lower()
        if any(word in query for word in ["calculate", "sum", "percentage", "+", "-"]):
            state["intent"] = "calculation"
        elif any(word in query for word in ["error", "failed", "debug", "issue"]):
            state["intent"] = "debugging"
        else:
            state["intent"] = "knowledge_qa"
        state["debug_trace"].append(f"Intent classified as {state['intent']}")
        return state

    def retrieve_context(self, state: AgentState) -> AgentState:
        docs = self.store.search(state["query"], top_k=3)
        state["retrieved_docs"] = docs
        state["debug_trace"].append(f"Retrieved {len(docs)} documents")
        return state

    def maybe_use_tool(self, state: AgentState) -> AgentState:
        intent = state.get("intent")
        if intent == "calculation":
            state["tool_name"] = "calculator"
            state["tool_output"] = self.tools.run("calculator", state["query"])
        elif intent == "debugging":
            state["tool_name"] = "debug_ai_failure"
            state["tool_output"] = self.tools.run("debug_ai_failure", state["query"])
        else:
            state["tool_name"] = None
            state["tool_output"] = "No external tool required."
        state["debug_trace"].append(f"Tool selected: {state.get('tool_name')}")
        return state

    def generate_answer(self, state: AgentState) -> AgentState:
        context = "\n\n".join(
            [f"Source: {doc['source']} | {doc['text']}" for doc in state.get("retrieved_docs", [])]
        )
        prompt = ANSWER_TEMPLATE.format(
            query=state["query"],
            context=context or "No context found.",
            tool_output=state.get("tool_output", ""),
        )
        state["answer"] = self.llm.generate(prompt)
        state["debug_trace"].append("Answer generated")
        return state
