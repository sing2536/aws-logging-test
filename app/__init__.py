"""Application factory module."""
from flask import Flask
from app.config.config import DB_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from app.models import init_db
from app.routes import init_routes

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    
    # Initialize the database
    init_db(app)
    
    # Register routes
    init_routes(app)
    
    return app 