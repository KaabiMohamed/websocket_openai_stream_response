from fastapi import APIRouter, WebSocket
from fastapi.responses import StreamingResponse
from services.chat_service import send_message

router = APIRouter()


@router.websocket("/websocket-chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        generator = send_message(data)
        async for message in generator:
            await websocket.send_text(message)


@router.get("/stream-chat")
async def stream_chat(message: str):
    generator = send_message(message)
    return StreamingResponse(generator, media_type="text/event-stream")
