import uuid
from src.kopi.domain.entities import Message
from src.kopi.infrastructure.supabase_messages_repository import SupabaseMessagesRepository

def test_supabase_messages_repository(settings):
    repo = SupabaseMessagesRepository(settings.supabase_url, settings.supabase_key, settings.supabase_table)
    msg = Message(conversation_id=str(uuid.uuid4()), role="user", message="Test message")
    # Save a message
    import asyncio
    assert asyncio.run(repo.save_message(msg)) is True
    # Retrieve the message
    messages = asyncio.run(repo.get_last_messages(str(msg.conversation_id)))
    assert len(messages) == 1
    assert messages[0].conversation_id == str(msg.conversation_id)
    assert messages[0].message == "Test message"
