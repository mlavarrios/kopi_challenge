import asyncio
from src.kopi.application.entities import MessageDTO
from src.kopi.domain.debates_service import DebatesService
from src.kopi.domain.entities import Debate
from src.kopi.infrastructure.ai_repository import AIRepository
from src.kopi.infrastructure.entities import LLMAnswer
from src.kopi.infrastructure.supabase_messages_repository import SupabaseMessagesRepository
from settings import Settings


def test_debates_service_debate(monkeypatch):
    class DummyAIRepository(AIRepository):
        async def generate_response(self, prompt: str):
            return LLMAnswer(text="Counterargument")
    class DummyMessagesRepository(SupabaseMessagesRepository):
        def __init__(self):
            pass
        async def get_last_messages(self, conversation_id):
            return []
        async def save_message(self, message):
            return True
    debates_service = DebatesService(DummyMessagesRepository(), DummyAIRepository(Settings.get_settings()))
    message_dto = MessageDTO(message="Test", conversation_id=None)
    debate = asyncio.run(debates_service.debate(message_dto))
    assert isinstance(debate, Debate)
    assert debate.messages[-1].role == "bot"