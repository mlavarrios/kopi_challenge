from typing import Annotated
from fastapi import Depends
from src.settings import Settings
from src.kopi.infrastructure.messages_repository import (
    MessagesRepository,
)
from src.kopi.infrastructure.supabase_messages_repository import (
    SupabaseMessagesRepository,
)
from src.kopi.infrastructure.json_messages_repository import JsonMessagesRepository

settings = Settings.get_settings()

class MessagesRepositoryFactory:
    @staticmethod
    def get_messages_repo(
        settings: Annotated[Settings, Depends(Settings.get_settings)]
    ):
        if settings.db_carrier == "json":
            return JsonMessagesRepository(settings.json_file_path)
        if settings.db_carrier == "supabase":
            return SupabaseMessagesRepository(
                settings.supabase_host,
                settings.supabase_port,
                settings.supabase_key,
                settings.supabase_table,
            )
        return MessagesRepository(settings.db_host, settings.db_port, settings.db_name, settings.db_collection)
