from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    hf_token: str

    class Config:
        env_file = ".env"

settings = Settings()
# Access the Hugging Face API key using settings.hf_api_key