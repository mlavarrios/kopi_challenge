

from fastapi.applications import FastAPI

from config.config import register_routers


def init_app() -> FastAPI:
    api = FastAPI()
    api = register_routers(api)

    return api


app = init_app()
