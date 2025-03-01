"""Database-related routes for the application."""
from flask import Blueprint, jsonify
import random
import string
from app.models import db
from app.models.user import User

db_bp = Blueprint('db', __name__)

@db_bp.route("/test")
def db_test():
    """Test database connection."""
    try:
        db.create_all()
        return jsonify({"message": "Database connection successful!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@db_bp.route("/info")
def db_info():
    """Get database information."""
    try:
        # Get database info
        engine = db.engine
        inspector = db.inspect(engine)
        
        # Get database name
        db_name = engine.url.database
        
        # Get all tables
        tables = inspector.get_table_names()
        
        # Get sample data from User table if it exists
        users = []
        if 'user' in [t.lower() for t in tables]:
            users = [{"id": user.id, "username": user.username} 
                    for user in User.query.limit(10).all()]
        
        return jsonify({
            "database_name": db_name,
            "tables": tables,
            "sample_users": users,
            "connection_info": str(engine.url).replace(":Siam2536@", ":****@")  # Hide password
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@db_bp.route("/add-users/<int:count>")
def add_users(count=1):
    """Add random users to the database."""
    try:
        if count > 100:
            return jsonify({"error": "Maximum 100 users can be created at once"}), 400
            
        new_users = []
        for _ in range(count):
            # Generate a random username
            random_username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user = User(username=random_username)
            db.session.add(user)
            new_users.append(random_username)
        
        db.session.commit()
        return jsonify({
            "message": f"Successfully added {count} random users",
            "users_added": new_users
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500 