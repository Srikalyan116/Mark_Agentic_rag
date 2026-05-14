from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Agentic RAG Assistant"
    env: str = "local"
    llm_provider: str = "local"
    openai_api_key: str | None = None
    azure_openai_endpoint: str | None = None
    azure_openai_api_key: str | None = None
    azure_openai_deployment: str | None = None

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
