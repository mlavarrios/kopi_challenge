import uuid
from pymongo import AsyncMongoClient
from kopi.domain.entities import Message

class MessagesRepository:
    def __init__(self, host: str, port: int, db_name: str, db_collection: str):
        self.client = AsyncMongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[db_collection]

    async def get_last_messages(self, conversation_id: str, limit: int = 5) -> list[Message]:
        query = {"conversation_id": conversation_id}
        raw_messages = await self.collection.find(query).sort("timestamp", -1).limit(limit).to_list(length=limit)
        messages = [Message(**msg) for msg in raw_messages]

        return messages

    async def save_message(self, message: Message, conversation_id: str|None) -> str:
        """Save a message to the database and return its inserted ID."""
        print("Saving message:", message)
        message_dict = message.model_dump()
        if not conversation_id:
            conversation_id = str(uuid.uuid4())
        message_dict["conversation_id"] = conversation_id
        try:
            await self.collection.insert_one(message_dict)
        except Exception as e:
            print("Error saving message:", e)
        return conversation_id