from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.api.api import api_router
from app.core.database import engine
from app.models.base import Base

settings = get_settings()

app = FastAPI(
    title="AI Career Companion API",
    description="Backend API for AI Career Companion platform",
    version=settings.VERSION,
)

# mount versioned API router
app.include_router(api_router, prefix=settings.API_V1_STR)

# create database tables on startup (useful for SQLite/tests)
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": settings.VERSION}