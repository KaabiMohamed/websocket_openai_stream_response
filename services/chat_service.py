import asyncio
from typing import AsyncIterable
from config.settings import settings
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


async def send_message(content: str) -> AsyncIterable[str]:
    """
    Sends a message to the ChatOpenAI model and yields the response tokens asynchronously.

    Args:
        content (str): The content of the message to be sent to the chat model.

    Yields:
        AsyncIterable[str]: An asynchronous iterable of response tokens from the chat model.

    Raises:
        Exception: Propagates exceptions caught during the asynchronous generation and streaming process.
    """
    # Initialize the callback handler for streaming responses
    callback = AsyncIteratorCallbackHandler()

    # Create a ChatOpenAI model instance with the necessary configurations
    model = ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY,
        streaming=True,
        verbose=True,
        callbacks=[callback],
    )

    # Create and start an asynchronous task to generate responses
    task = asyncio.create_task(model.agenerate(messages=[[HumanMessage(content=content)]]))

    try:
        # Stream response tokens from the callback as they become available
        async for token in callback.aiter():
            yield token
    except Exception as e:
        # Handle any exceptions that occur during response streaming
        print(f"Caught exception: {e}")
    finally:
        # Ensure the callback's completion flag is set when done
        callback.done.set()

    # Wait for the task to complete before exiting the function
    await task
