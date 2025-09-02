from typing import Annotated
from fastapi import Depends
from src.settings import Settings
from src.kopi.infrastructure.messages_repository import (
    MessagesRepository,
)

settings = Settings.get_settings()

class MessagesRepositoryFactory:
    @staticmethod
    def get_messages_repo(
        settings: Annotated[Settings, Depends(Settings.get_settings)]
    ):
        return MessagesRepository(settings.db_host, settings.db_port, settings.db_name, settings.db_collection)
