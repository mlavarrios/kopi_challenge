import json
from src.kopi.domain.entities import Message


class JsonMessagesRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path

    async def get_last_messages(self, conversation_id: str) -> list[Message]:
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                raw_messages = data[conversation_id]
                return [Message(**item) for item in raw_messages]
        except Exception as e:
            print("Error retrieving messages:", e)
            raise(e)

    async def save_message(self, message: Message, conversation_id: str|None) -> str:
        import uuid;
        message.created_at = None
        if not conversation_id:
            conversation_id = str(uuid.uuid4())
        try:
            with open(self.file_path, "r+") as f:
                data = json.load(f)
                if conversation_id not in data:
                    data[conversation_id] = []
                data[conversation_id].append(message.dict())
                f.seek(0)
                json.dump(data, f)
            return conversation_id
        except Exception as e:
            print("Error saving message:", e)
            raise(e)
