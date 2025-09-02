from typing import Optional
from pydantic import BaseModel

class Message(BaseModel):
    role: str
    message: Optional[str]

class Debate(BaseModel):
    conversation_id: str
    messages: list[Message]