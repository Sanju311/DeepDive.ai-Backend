from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1", tags=["API"])

@api_router.get("/status")
async def api_status():
    """API status endpoint"""
    return {
        "api_version": "1.0.0",
        "status": "running",
        "endpoints": {
            "root": "/",
            "health": "/health",
            "interview": "/interview"
        }
    }

@api_router.get("/version")
async def get_version():
    """Get API version information"""
    return {
        "version": "1.0.0",
        "name": "Interview AI Backend",
        "description": "Backend API for Interview AI application"
    }





