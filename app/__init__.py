"""Application factory module."""
from fastapi import FastAPI
from app.config.config import DB_URI
from app.models import init_db
from app.routes import init_routes

def create_app():
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="AWS Logging Test",
        description="A FastAPI application for testing AWS logging",
        version="0.1.0"
    )
    
    # Initialize the database
    init_db()
    
    # Register routes
    init_routes(app)
    
    return app 