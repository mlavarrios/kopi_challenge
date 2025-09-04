from typing import Any
import configparser
import pathlib
import os
from pydantic import BaseModel


class Settings(BaseModel):
    gemini_api_key: str = ""
    db_host: str = ""
    db_port: int = 0
    db_name: str = ""
    db_collection: str = ""
    db_username: str = ""
    db_password: str = ""

    def __init__(self, **values: Any):
        super().__init__(**values)
        current_dir = pathlib.Path(__file__).parent
        config = configparser.ConfigParser(os.environ)
        config.read([str(current_dir) + "/application.ini", "application.ini"])
        self.gemini_api_key = config.get("gemini", "gemini_api_key")
        self.db_host = config.get("database", "db_host")
        self.db_port = int(config.get("database", "db_port"))
        self.db_name = config.get("database", "db_name")
        self.db_collection = config.get("database", "db_collection")
        self.db_username = config.get("database", "db_username")
        self.db_password = config.get("database", "db_password")

    @staticmethod
    def get_settings():
        return Settings()
