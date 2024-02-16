from pydantic import BaseModel
from typing import Optional
from .enums import StatusEnum


class Metadata(BaseModel):
    status: Optional[StatusEnum] = None
    name: Optional[str] = None
    mood_index: Optional[float] = None
