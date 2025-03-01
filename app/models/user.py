"""User model for the application."""
from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr


class UserBase(SQLModel):
    """Base model with shared fields."""
    username: str = Field(index=True, unique=True, min_length=3, max_length=50)
    email: Optional[str] = Field(default=None, index=True, unique=True)
    full_name: Optional[str] = Field(default=None)
    is_active: bool = Field(default=True)


class User(UserBase, table=True):
    """User model representing application users."""
    __tablename__ = "users"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)
    
    def __repr__(self):
        return f'<User {self.username}>'


class UserCreate(UserBase):
    """Schema for creating a new user."""
    pass


class UserResponse(UserBase):
    """Schema for user responses."""
    id: int
    created_at: datetime 