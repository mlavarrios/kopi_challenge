from supabase import create_client, Client
from src.kopi.domain.entities import Message

class SupabaseMessagesRepository:
    def __init__(self, url: str, key: str, table: str):
        self.url = url
        self.key = key
        self.client: Client = create_client(supabase_url=self.url, supabase_key=self.key)
        self.db = self.client.table(table)

    async def get_last_messages(self, conversation_id: str) -> list[Message]:
        try:
            raw_messages = (self.db.select("*")
                .eq("conversation_id", conversation_id)
                .limit(10)
                .execute())
            messages = [Message(**msg) for msg in raw_messages.data]
            return messages
        except Exception as e:
            print("Error retrieving messages:", e)
            raise(e)

    async def save_message(self, message: Message) -> bool:
        message_dict = message.model_dump()
        try:
            self.db.insert(message_dict).execute()
            return True
        except Exception as e:
            print("Error saving message:", e)
            raise(e)
