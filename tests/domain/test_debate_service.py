import asyncio
from unittest.mock import AsyncMock
from src.kopi.application.entities import MessageDTO
from src.kopi.domain.debates_service import DebatesService
from src.kopi.domain.entities import Debate


def test_debates_service_debate(monkeypatch):
    debates_service = DebatesService(messages_repository=AsyncMock(), ai_repository=AsyncMock())
    debates_service.messages_repository.get_last_messages = AsyncMock(return_value=[])
    debates_service.messages_repository.save_message = AsyncMock(return_value=True)
    debates_service.ai_repository.generate_response = AsyncMock(return_value=AsyncMock(text="This is a bot response"))

    message_dto = MessageDTO(message="Test", conversation_id=None)
    
    debate = asyncio.run(debates_service.debate(message_dto))

    assert isinstance(debate, Debate)
    assert debate.messages[-1].role == "bot"