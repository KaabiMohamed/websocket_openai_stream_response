from typing import Optional

from pydantic import BaseModel

from .metadata import Metadata


class ChatResponse(BaseModel):
    id: str
    object: str
    content: Optional[str] = None
    finish_reason: Optional[str] = None
    metadata: Optional[Metadata] = None

    def to_json(self):
        return self.json()
