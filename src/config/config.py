from fastapi import FastAPI

from src.kopi.application import debate_controller


def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(debate_controller.router, prefix="")
    return app
