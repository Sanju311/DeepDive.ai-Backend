# Routes package
from fastapi import APIRouter
from .interview import router as interview_router

# Main router that combines all sub-routers
router = APIRouter()

@router.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to Interview AI Backend API"}

# Include all sub-routers
router.include_router(interview_router)

__all__ = ["router", "interview_router"]
