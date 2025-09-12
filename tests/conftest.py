import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.settings import Settings


@pytest.fixture(scope="session")
def settings():
    settings = Settings.get_settings()
    settings.supabase_table = "test"
    yield settings


@pytest.fixture(scope="session", autouse=True)
def client():
    client = TestClient(app)
    yield client
