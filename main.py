from dotenv import load_dotenv
from elevenlabs import ElevenLabs


from settings import settings

load_dotenv()


def main(req, res, log, error):
    return res.json({"Request": req})


elevenlabs = ElevenLabs(
    api_key=settings.ELEVENLABS_API_KEY,
)
WEBHOOK_SECRET = settings.WEBHOOK_SECRET
