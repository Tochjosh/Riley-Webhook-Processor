from dotenv import load_dotenv
from elevenlabs import ElevenLabs


from config import settings

load_dotenv()

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
