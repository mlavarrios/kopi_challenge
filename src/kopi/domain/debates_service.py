from datetime import datetime
from src.kopi.application.entities import MessageDTO
from src.kopi.domain.entities import Debate, Message
from src.kopi.infrastructure.ai_repository import AIRepository
from src.kopi.infrastructure.messages_repository import MessagesRepository


class DebatesService:
    def __init__(self, messages_repository: MessagesRepository, ai_repository: AIRepository):
        self.messages_repository = messages_repository
        self.ai_repository = ai_repository

    async def debate(self, message: MessageDTO) -> Debate:
        last_messages = []
        user_message = Message(role="user", message=message.message, created_at=datetime.now())
        if message.conversation_id:
            last_messages = await self.messages_repository.get_last_messages(message.conversation_id)
        last_messages.append(user_message)

        prompt = """
        All of your responses should be related to the original conversation topic and stand your ground.
        The goal is to convince the other side of your view.
        You are a participant in a debate.
        These are the messages:
        """

        prompt = prompt + "\n\n".join("role: {}\ncontent: {}".format(msg.role, msg.message) for msg in last_messages)

        print("Prompt sent to AI:", prompt)

        answer = await self.ai_repository.generate_response(prompt=prompt)

        conversation_id = await self.messages_repository.save_message(user_message, conversation_id=message.conversation_id)
        
        bot_message = Message(role="bot", message=answer.text, created_at=datetime.now())
        conversation_id = await self.messages_repository.save_message(bot_message, conversation_id=conversation_id)

        last_messages.append(bot_message)

        return Debate(
            conversation_id=conversation_id,
            messages=last_messages
        )