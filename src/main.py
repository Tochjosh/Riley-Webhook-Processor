from dotenv import load_dotenv
from elevenlabs import ElevenLabs


from src.settings import settings

load_dotenv()


def main(req, res, log, error):
    return res.json({
    "message": "Function is running",
    "method": req.method,
    "path": req.path
})


elevenlabs = ElevenLabs(
    api_key=settings.ELEVENLABS_API_KEY,
)
WEBHOOK_SECRET = settings.WEBHOOK_SECRET
