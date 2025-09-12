from datetime import datetime
import uuid
from src.kopi.application.entities import MessageDTO
from src.kopi.domain.entities import Debate, Message
from src.kopi.infrastructure.ai_repository import AIRepository
from src.kopi.infrastructure.supabase_messages_repository import SupabaseMessagesRepository


class DebatesService:
    def __init__(self, messages_repository: SupabaseMessagesRepository, ai_repository: AIRepository):
        self.messages_repository = messages_repository
        self.ai_repository = ai_repository

    async def debate(self, message: MessageDTO) -> Debate:
        last_messages = []
        if message.conversation_id:
            last_messages = await self.messages_repository.get_last_messages(message.conversation_id)
            conversation_id = message.conversation_id
        else:
            conversation_id = str(uuid.uuid4())
        user_message = Message(conversation_id=conversation_id, role="user", message=message.message)

        last_messages.append(user_message)

        prompt = """
        You are a participant in a debate.
        All of your responses should be related to the original conversation topic and stand your ground.
        The goal is to go against the user's opinion and provide counterarguments.
        Always bring facts and data to support your arguments.
        Never agree with the user.
        These are the messages:
        """

        prompt = prompt + "\n\n".join("role: {}\ncontent: {}".format(msg.role, msg.message) for msg in last_messages)

        print("Prompt sent to AI:", prompt)

        answer = await self.ai_repository.generate_response(prompt=prompt)

        await self.messages_repository.save_message(user_message)

        bot_message = Message(conversation_id=conversation_id, role="bot", message=answer.text)

        await self.messages_repository.save_message(bot_message)

        last_messages.append(bot_message)

        return Debate(
            conversation_id=conversation_id,
            messages=last_messages
        )
