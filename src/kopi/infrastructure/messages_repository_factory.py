from typing import Annotated
from fastapi import Depends
from src.settings import Settings
from src.kopi.infrastructure.supabase_messages_repository import (
    SupabaseMessagesRepository,
)

settings = Settings.get_settings()

class MessagesRepositoryFactory:
    @staticmethod
    def get_messages_repo(
        settings: Annotated[Settings, Depends(Settings.get_settings)]
    ):
        return SupabaseMessagesRepository(
            settings.supabase_url,
            settings.supabase_key,
            settings.supabase_table,
        )
