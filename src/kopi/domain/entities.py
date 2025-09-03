from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Message(BaseModel):
    role: str
    message: Optional[str]
    created_at: datetime

class Debate(BaseModel):
    conversation_id: str
    messages: list[Message]