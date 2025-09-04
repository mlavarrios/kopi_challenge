from typing import Annotated
from fastapi import APIRouter, Depends
from src.kopi.infrastructure.ai_repository_factory import AIRepositoryFactory
from src.kopi.infrastructure.ai_repository import AIRepository
from src.kopi.infrastructure.messages_repository import MessagesRepository
from src.kopi.infrastructure.messages_repository_factory import MessagesRepositoryFactory
from src.kopi.application.entities import MessageDTO
from src.kopi.domain.debates_service import DebatesService


router = APIRouter()

@router.get("/health")
async def health_check():
    return "The health check is OK."

@router.post("/")
async def debate(
    message: MessageDTO,
    ai_repository: Annotated[AIRepository, Depends(AIRepositoryFactory.get_ai_repo)],
    messages_repository: Annotated[
        MessagesRepository,
        Depends(MessagesRepositoryFactory.get_messages_repo),
    ],
):
    debates_service = DebatesService(messages_repository, ai_repository)
    try:
        response = await debates_service.debate(message)
    except Exception as e:
        print("Error occurred while debating:", e)
        return {"error": str(e)}
    return response
