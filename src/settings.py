from typing import Any
import configparser
import pathlib
import os
from pydantic import BaseModel
from langchain_community.chat_models import ChatOpenAI


class Settings(BaseModel):
    vector_database_host: str = ""
    vector_database_port: int = None
    vector_database_grpc_port: int = None
    vector_database_collection_name: str = ""
    gemini_api_key: str = ""
    db_host: str = ""
    db_port: int = None
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

    @property
    def get_db_connection_url(self):
        return f"mongodb://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}"

    def get_model_config(self):
        return ModelsConfig(settings=self)


class ModelsConfig:
    def __init__(self, settings: Settings, bot_id: str | None = None):
        self.openai = ChatOpenAI(
            name="gpt-4.1-mini"
        )

        # self.llm_config = LLMConfig(
        #     prompt_id=DEFAULT_PROMPT_ID,
        #     llm=self.openai,
        #     chain_type="stuff",
        #     return_source_documents=True,
        #     access_method="langchain",  # openai_direct #TODO: find a better approach
        #     search_kwargs={"k": DEFAULT_TOTAL_MATCHES},
        # )
