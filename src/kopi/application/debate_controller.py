from typing import Annotated
from fastapi import APIRouter, Depends
from src.kopi.infrastructure.ai_repository import AIRepository
from src.kopi.infrastructure.messages_repository import MessagesRepository
from src.kopi.infrastructure.messages_repository_factory import MessagesRepositoryFactory
from src.kopi.application.entities import MessageDTO
from src.kopi.domain.debates_service import DebatesService
from src.settings import Settings


router = APIRouter()

@router.get("/health")
async def health_check():
    return "The health check is OK."

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
