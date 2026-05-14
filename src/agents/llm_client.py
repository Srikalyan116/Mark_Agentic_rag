from src.config.settings import settings


class LLMClient:
    """Minimal LLM client with local fallback.

    Replace generate() internals with OpenAI/Azure OpenAI SDK calls when keys are available.
    """

    def generate(self, prompt: str) -> str:
        if settings.llm_provider == "local":
            return self._local_answer(prompt)
        return self._local_answer(prompt)

    def _local_answer(self, prompt: str) -> str:
        return (
            "This is a local fallback response. The system retrieved relevant context, "
            "selected tools when required, and generated a grounded answer. "
            "For production, connect OpenAI, Azure OpenAI, Anthropic, or an open-source model.\n\n"
            f"Prompt preview:\n{prompt[:1000]}"
        )
