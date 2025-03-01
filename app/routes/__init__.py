"""Routes initialization."""
from fastapi import FastAPI

def init_routes(app: FastAPI):
    """Register all routes with the app."""
    # Import the route modules
    from app.routes.main import router as main_router
    from app.routes.db import router as db_router
    
    # Include routers
    app.include_router(main_router)
    app.include_router(db_router, prefix="/db") 