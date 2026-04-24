import os
import functools
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ELEVENLABS_API_KEY: str | None
    WEBHOOK_SECRET: str | None

    def __init__(self):
        self.ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
        self.WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

    def validate(self):
        if not self.ELEVENLABS_API_KEY:
            raise ValueError("ELEVENLABS_API_KEY is not set")
        if not self.WEBHOOK_SECRET:
            raise ValueError("WEBHOOK_SECRET is not set")


@functools.lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    settings.validate()
    return settings

settings = get_settings()
 
