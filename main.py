import os
import functools

from dotenv import load_dotenv
from elevenlabs import ElevenLabs

load_dotenv()


class Settings:
    ELEVENLABS_API_KEY: str | None
    WEBHOOK_SECRET: str | None
    ELEVENLABS_API_KEY: str | None

    def __init__(self):
        self.WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
        self.ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

    def validate(self):
        if not self.WEBHOOK_SECRET:
            raise ValueError("WEBHOOK_SECRET is not set")
        if not self.ELEVENLABS_API_KEY:
            raise ValueError("ELEVENLABS_API_KEY is not set")


@functools.lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    # settings.validate()
    return settings


settings = get_settings()

# elevenlabs = ElevenLabs(
#     api_key=settings.ELEVENLABS_API_KEY,
# )


def main(req, res, log, error):

    # payload = req.body
    # signature = req.headers.get("elevenlabs-signature")
    # try:
    #     event = elevenlabs.webhooks.construct_event(
    #         rawBody=payload.decode("utf-8"),
    #         sig_header=signature,
    #         secret=settings.WEBHOOK_SECRET,
    #     )
    # except Exception as e:
    #     return res.json({
    #         "error": "Invalid signature"
    #     }, 401)
    # if event.get("type") == "post_call_transcription":
    #     print(f"Received transcription: {event.get('data')}")
    return res.json(
        {
            "message": "Function is running",
            "method": req.method,
            "path": req.path,
        }
    )
