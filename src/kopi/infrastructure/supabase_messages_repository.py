import uuid
from supabase import create_client, Client
from src.kopi.domain.entities import Message

class SupabaseMessagesRepository:
    def __init__(self, host: str, port: int, key: str, table: str):
        self.host = host
        self.port = port
        self.key = key
        self.client: Client = create_client(supabase_url=f"https://{self.host}:{self.port}", supabase_key=self.key)
        self.db = self.client.table(table)

    async def get_last_messages(self, conversation_id: str, limit: int = 5) -> list[Message]:
        # Implementation for retrieving messages from Supabase
        try:
            raw_messages = (self.db.select(conversation_id).execute())
            messages = [Message(**msg) for msg in raw_messages.data]
            return messages
        except Exception as e:
            print("Error retrieving messages:", e)
            raise(e)

    async def save_message(self, message: Message, conversation_id: str|None) -> str:
        # Implementation for creating a message in Supabase
        import pdb; pdb.set_trace()
        if not conversation_id:
            conversation_id = str(uuid.uuid4())
        message_dict = message.model_dump(mode="json")
        message_dict["conversation_id"] = conversation_id
        try:
            self.db.insert(message_dict).execute()
            return conversation_id
        except Exception as e:
            print("Error saving message:", e)
            raise(e)