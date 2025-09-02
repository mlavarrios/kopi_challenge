from typing import Annotated
from fastapi import Depends
from src.settings import Settings
from src.kopi.infrastructure.ai_repository import (
    AIRepository,
)

settings = Settings.get_settings()

class AIRepositoryFactory:
    @staticmethod
    def get_ai_repo(
        settings: Annotated[Settings, Depends(Settings.get_settings)]
    ):
        return AIRepository(settings=settings)
