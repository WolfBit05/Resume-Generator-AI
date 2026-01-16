from pydantic import BaseSettings

class Settings(BaseSettings):
    hf_api_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
# Access the Hugging Face API key using settings.hf_api_key