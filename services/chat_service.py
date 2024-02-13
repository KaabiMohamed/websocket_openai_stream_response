import asyncio
from typing import AsyncIterable
from config.settings import settings
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


async def send_message(content: str) -> AsyncIterable[str]:
    callback = AsyncIteratorCallbackHandler()
    model = ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY,
        streaming=True,
        verbose=True,
        callbacks=[callback],
    )
    task = asyncio.create_task(model.agenerate(messages=[[HumanMessage(content=content)]]))
    try:
        async for token in callback.aiter():
            yield token
    except Exception as e:
        print(f"Caught exception: {e}")
    finally:
        callback.done.set()
    await task
