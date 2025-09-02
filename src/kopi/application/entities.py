from typing import Optional
from pydantic import BaseModel
from kopi.domain.entities import Message

class MessageDTO(BaseModel):
    conversation_id: Optional[str]
    message: str

class ResponseDTO(BaseModel):
    conversation_id: str
    messages: list[Message]