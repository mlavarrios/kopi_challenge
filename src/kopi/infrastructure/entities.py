from typing import Optional
from pydantic import BaseModel


class LLMAnswer(BaseModel):
    text: Optional[str]
