"""Main routes for the application."""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def index():
    """Home page route."""
    return {"message": "Your FastAPI App Works!"}