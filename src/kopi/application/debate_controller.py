from typing import Annotated
from fastapi import APIRouter, Depends
from kopi.infrastructure.ai_repository import AIRepository
from kopi.infrastructure.messages_repository import MessagesRepository
from kopi.infrastructure.messages_repository_factory import MessagesRepositoryFactory
from kopi.application.entities import MessageDTO
from kopi.domain.debates_service import DebatesService
from settings import Settings


router = APIRouter()

@router.post("/")
async def debate(
    message: MessageDTO,
    settings: Annotated[Settings, Depends(Settings.get_settings)],
    messages_repository: Annotated[
        MessagesRepository,
        Depends(MessagesRepositoryFactory.get_messages_repo),
    ],
):
    ai_repository = AIRepository(settings)
    debates_service = DebatesService(messages_repository, ai_repository)
    response = await debates_service.debate(message)
    return response
