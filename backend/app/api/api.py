"""Main router that includes all API endpoints"""
from fastapi import APIRouter
from app.api import auth, resume, users

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(resume.router, prefix="/resume", tags=["resume"])
api_router.include_router(users.router, prefix="/users", tags=["users"])