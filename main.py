import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

def create_app() -> FastAPI:
    """Application factory pattern for creating FastAPI app"""
    
    app = FastAPI(
        title="Interview AI Backend",
        description="Backend API for Interview AI application",
        version="1.0.0"
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Configure this properly for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include all routes
    app.include_router(router)

    return app



# Create FastAPI instance using the app factory
app = create_app()

