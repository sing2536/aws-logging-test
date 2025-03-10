"""User model for the application."""
from app.models import db

class User(db.Model):
    """User model representing application users."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username 