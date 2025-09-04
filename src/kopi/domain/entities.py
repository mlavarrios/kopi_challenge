from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Message(BaseModel):
    conversation_id: str
    role: str
    message: str
    created_at: Optional[datetime] = None

class Debate(BaseModel):
    conversation_id: str
    messages: list[Message]