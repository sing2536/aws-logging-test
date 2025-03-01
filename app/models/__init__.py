"""Database initialization."""
from sqlmodel import SQLModel, create_engine, Session
from app.config.config import DB_URI

# Create SQLModel engine
engine = create_engine(DB_URI)

def recreate_db():
    """Drop all tables and recreate them."""
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)

def init_db():
    """Initialize the database."""
    # Import all models here to ensure they are registered with SQLModel
    from app.models.user import User
    
    # Drop and recreate all tables 
    # Comment out the recreate_db() call after initial setup if you want to preserve data
    recreate_db()
    
    # If you only want to create missing tables without dropping existing ones, use this:
    # SQLModel.metadata.create_all(bind=engine)

def get_db():
    """Get database session."""
    with Session(engine) as session:
        yield session 