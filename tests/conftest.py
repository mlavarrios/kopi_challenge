import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture(scope="session", autouse=True)
def client():
    client = TestClient(app)
    yield client
