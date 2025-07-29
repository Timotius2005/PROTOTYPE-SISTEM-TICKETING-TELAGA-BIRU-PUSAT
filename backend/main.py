
from fastapi import FastAPI
from app.api.routes import sync

app = FastAPI()

app.include_router(sync.router, prefix="/sync", tags=["Sync"])
