import uvicorn
from fastapi import FastAPI
from dishka.integrations.fastapi import setup_dishka
from src.core.di.ioc_container import get_container


def initialize_app(_app: FastAPI) -> FastAPI:
    setup_dishka(get_container(), _app)
    return _app


app = initialize_app(FastAPI(
    title="In-Tourist Consumer",
    description="This microservice contains promo_code and payment",
    version='0.0.2'
))

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, workers=4)
