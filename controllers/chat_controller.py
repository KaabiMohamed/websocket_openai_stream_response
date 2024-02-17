import secrets

from fastapi import APIRouter, WebSocket
from fastapi.responses import StreamingResponse
from starlette.websockets import WebSocketDisconnect

from monitoring.custom_metrics import REQUEST_COUNTER, MOOD_CHECK
from monitoring.mood_check import estimate_mood
from services.chat_service import send_message
from dto.chat_response import ChatResponse
from dto.metadata import Metadata
from dto.enums import StatusEnum, FinishReasonEnum

router = APIRouter()


@router.websocket("/websocket-chat/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    """
    Handles WebSocket chat connections, receiving messages, and sending responses.
    Increments request counter, updates mood gauge based on message sentiment, and
    streams chat responses back to the client.
    """
    await websocket.accept()
    print("Client ", client_id, " connected")
    try:
        while True:
            # Receives text data from the client over WebSocket
            data = await websocket.receive_text()
            # Generates a unique ID for the message chunks using a secure token
            id = secrets.token_urlsafe(10)
            # Increments the custom Prometheus counter for tracking requests
            REQUEST_COUNTER.labels("websocket_endpoint", "/websocket-chat").inc()
            # Estimates the mood of the received message
            mood_index = estimate_mood(data)
            # Updates the mood gauge metric for the current user
            MOOD_CHECK.labels(user=client_id).set(mood_index)
            # Sends the received message for processing and awaits the response
            async for message in send_message(data):
                await websocket.send_text(ChatResponse(id=id, object="chat.completion", content=message).to_json())
            # Once the chat is complete, sends a final message
            await websocket.send_text(ChatResponse(
                id=id,
                object="chat.completion",
                finish_reason=FinishReasonEnum.finish,
                metadata=Metadata(status=StatusEnum.task_done, name=client_id, mood_index=mood_index)
            ).to_json())
    except WebSocketDisconnect:
        print("Client ", client_id, " disconnected")


@router.get("/stream-chat")
async def stream_chat(message: str):
    """
     Streams chat responses for a given message via HTTP, incrementing the request counter.
     Returns a StreamingResponse with the chat messages as an event stream.
     """
    # Increments the custom Prometheus counter for this endpoint
    REQUEST_COUNTER.labels("stream_chat", "/stream-chat").inc()
    # Initiates streaming of chat responses as an event stream
    return StreamingResponse(send_message(message), media_type="text/event-stream")
