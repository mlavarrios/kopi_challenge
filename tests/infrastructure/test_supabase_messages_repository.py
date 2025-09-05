import pytest
from src.kopi.domain.entities import Message
from src.kopi.infrastructure.supabase_messages_repository import SupabaseMessagesRepository
from unittest.mock import patch

def test_supabase_messages_repository():
    # Use a dict as the mock database
    db = {}

    async def mock_save_message(self, message):
        db.setdefault(message.conversation_id, []).append(message)
        return True

    async def mock_get_last_messages(self, conversation_id):
        return db.get(conversation_id, [])

    with patch.object(SupabaseMessagesRepository, 'save_message', mock_save_message), \
         patch.object(SupabaseMessagesRepository, 'get_last_messages', mock_get_last_messages):
        repo = SupabaseMessagesRepository("https://url", "key", "table")
        msg = Message(conversation_id="id", role="user", message="msg")
        # Save a message
        import asyncio
        assert asyncio.run(repo.save_message(msg)) is True
        # Retrieve the message
        messages = asyncio.run(repo.get_last_messages("id"))
        assert len(messages) == 1
        assert messages[0].conversation_id == "id"
        assert messages[0].message == "msg"
