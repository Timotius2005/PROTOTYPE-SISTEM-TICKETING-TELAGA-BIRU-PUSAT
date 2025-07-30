from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api.routes import sync

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(sync.router, prefix="/sync", tags=["Sync"])
