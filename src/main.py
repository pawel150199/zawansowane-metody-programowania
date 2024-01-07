from sys import prefix
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.api import api_router
from src.core.settings import settings

app = FastAPI(title=settings.PROJECT_NAME, openapi_url="/openapi.json")

if settings.BACKEND_CORS_ORIGINS:

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)
