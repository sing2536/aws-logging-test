"""Database initialization."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    """Initialize the database with the Flask app."""
    db.init_app(app)
    
    # Create all database tables defined in models
    with app.app_context():
        # Drop all tables first
        db.drop_all()
        # Then recreate all tables
        db.create_all() 