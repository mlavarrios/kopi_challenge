from typing import Any
import configparser
import pathlib
import os
from pydantic import BaseModel


class Settings(BaseModel):
    gemini_api_key: str = ""
    supabase_url: str = ""
    supabase_key: str = ""
    supabase_table: str = ""

    def __init__(self, **values: Any):
        super().__init__(**values)
        current_dir = pathlib.Path(__file__).parent
        config = configparser.ConfigParser(os.environ)
        config.read([str(current_dir) + "/application.ini", "application.ini"])
        self.gemini_api_key = config.get("gemini", "gemini_api_key")
        self.supabase_url = config.get("supabase", "supabase_url")
        self.supabase_key = config.get("supabase", "supabase_key", fallback="postgres")
        self.supabase_table = "messages"

    @staticmethod
    def get_settings():
        return Settings()
