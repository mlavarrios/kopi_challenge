from src.kopi.infrastructure.ai_repository import AIRepository
from src.kopi.infrastructure.ai_repository_factory import AIRepositoryFactory
from src.kopi.infrastructure.entities import LLMAnswer
from src.kopi.infrastructure.messages_repository_factory import MessagesRepositoryFactory
from src.kopi.infrastructure.supabase_messages_repository import SupabaseMessagesRepository
from settings import Settings


def test_debate_endpoint(monkeypatch, client):
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
    monkeypatch.setattr(AIRepositoryFactory, "get_ai_repo", lambda: DummyAIRepository(Settings.get_settings()))
    monkeypatch.setattr(MessagesRepositoryFactory, "get_messages_repo", lambda: DummyMessagesRepository())
    payload = {"conversation_id": "", "message": "Test message"}
    response = client.post("/", json=payload)
    assert response.status_code == 200
    assert "messages" in response.json()
