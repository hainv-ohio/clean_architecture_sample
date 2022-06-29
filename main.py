import uvicorn

from fastapi import FastAPI
from .di import init_di

from src.presentation.apis.user_info import router as user_router

from src.config import cfg

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_di()

app.include_router(user_router, prefix=cfg.USER_API_PREFIX)

uvicorn.run(app, host=cfg.HOST, port=cfg.PORT)