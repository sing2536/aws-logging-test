"""Database-related routes for the application."""
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select, inspect, text
import random
import string
from typing import List as TypeList, Dict, Any, Optional
from datetime import datetime
from app.models import get_db, engine
from app.models.user import User, UserCreate, UserResponse

router = APIRouter()

@router.get("/test")
def db_test(db: Session = Depends(get_db)):
    """Test database connection."""
    try:
        # Just query something to test connection
        db.exec(text("SELECT 1"))
        return {"message": "Database connection successful!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/info")
def db_info(db: Session = Depends(get_db)):
    """Get database information."""
    try:
        # Get database info
        inspector = inspect(engine)
        
        # Get database name
        db_name = engine.url.database
        
        # Get all tables
        tables = inspector.get_table_names()
        
        # Get sample data from User table if it exists
        users = []
        if 'users' in [t.lower() for t in tables]:
            # Use SQLModel's select syntax
            statement = select(User).limit(10)
            users = [{"id": user.id, "username": user.username, "created_at": user.created_at} 
                    for user in db.exec(statement).all()]
        
        return {
            "database_name": db_name,
            "tables": tables,
            "sample_users": users,
            "connection_info": str(engine.url).replace(":Siam2536@", ":****@")  # Hide password
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/add-users/{count}")
def add_users(count: int = 1, db: Session = Depends(get_db)):
    """Add random users to the database."""
    try:
        if count > 100:
            raise HTTPException(status_code=400, detail="Maximum 100 users can be created at once")
            
        new_users = []
        for _ in range(count):
            # Generate a random username
            random_username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            # Generate a random email
            random_email = f"{random_username.lower()}@example.com"
            user = User(
                username=random_username,
                email=random_email,
                full_name=f"Test User {random_username}"
            )
            db.add(user)
            new_users.append(random_username)
        
        db.commit()
        return {
            "message": f"Successfully added {count} random users",
            "users_added": new_users
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users", response_model=TypeList[UserResponse])
def get_users(
    skip: int = 0, 
    limit: int = 10,
    active_only: bool = Query(default=False, description="Filter only active users"),
    db: Session = Depends(get_db)
):
    """Get a list of users with pagination."""
    query = select(User)
    
    if active_only:
        query = query.where(User.is_active == True)
        
    query = query.offset(skip).limit(limit)
    users = db.exec(query).all()
    return users

@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    # Check if username already exists
    existing_user = db.exec(select(User).where(User.username == user.username)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Username '{user.username}' already exists"
        )
    
    # Check if email already exists (if provided)
    if user.email:
        existing_email = db.exec(select(User).where(User.email == user.email)).first()
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Email '{user.email}' already exists"
            )
    
    # Create new user
    db_user = User.from_orm(user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get a specific user by ID."""
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return user

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete a user by ID."""
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    db.delete(user)
    db.commit()
    return None 