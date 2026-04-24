from h11._abnf import status_code
import os
from dotenv import load_dotenv
import httpx
from elevenlabs import ElevenLabs

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
FORWARD_URL = "https://peach.app.n8n.cloud/webhook/ai-receptionist/post-call"

client = httpx.AsyncClient(timeout=5.0)

elevenlabs = ElevenLabs(api_key=ELEVENLABS_API_KEY)


async def main(context):
    req = context.req
    res = context.res
    log = context.log
    error = context.error

    payload = req.bodyBinary
    signature = req.headers.get("elevenlabs-signature")

    if not signature:
        error("Missing signature header")
        return res.json({"error": "Missing signature"}, 400)

    try:
        raw_body = (
            payload.decode("utf-8") if isinstance(payload, bytes) else payload
        )

        event = elevenlabs.webhooks.construct_event(
            rawBody=raw_body,
            sig_header=signature,
            secret=WEBHOOK_SECRET,
        )
    except Exception as e:
        error(f"Signature verification failed: {str(e)}")

    event_type = event.get("type")
    log(f"Received event: {event_type}")

    if event_type == "post_call_transcription":
        try:
            response = await client.post(
                FORWARD_URL,
                json={"body": {"data": event.get("data")}},
            )
            log(f"Forwarded to n8n, status={response.status_code}")

        except httpx.RequestError as e:
            error(f"Failed to forward webhook: {str(e)}")

    return res.json({"status": "success"})
