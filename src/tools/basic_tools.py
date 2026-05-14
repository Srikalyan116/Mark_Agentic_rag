from src.tools.registry import Tool, ToolRegistry


def safe_calculator(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not set(expression).issubset(allowed):
        return "Invalid expression. Only basic arithmetic is allowed."
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as exc:
        return f"Calculator error: {exc}"


def explain_failure(error_text: str) -> str:
    return (
        "Debug checklist: verify environment variables, inspect API responses, "
        "check retrieval quality, log intermediate state, and add a regression test. "
        f"Observed issue: {error_text}"
    )


def build_default_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(
        Tool(
            name="calculator",
            description="Solves simple arithmetic expressions safely.",
            function=safe_calculator,
        )
    )
    registry.register(
        Tool(
            name="debug_ai_failure",
            description="Gives debugging steps for AI/LLM application failures.",
            function=explain_failure,
        )
    )
    return registry
