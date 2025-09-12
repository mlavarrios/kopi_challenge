from unittest.mock import Mock
from src.kopi.infrastructure.ai_repository import AIRepository
from src.kopi.infrastructure.ai_repository_factory import AIRepositoryFactory
from src.kopi.infrastructure.entities import LLMAnswer
from src.kopi.infrastructure.messages_repository_factory import MessagesRepositoryFactory
from src.kopi.infrastructure.supabase_messages_repository import SupabaseMessagesRepository


def test_debate_endpoint(client):
    
    payload = {"conversation_id": "1234", "message": "Test message"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    assert "messages" in response.json()
