"""Main routes for the application."""
from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    """Home page route."""
    return "Your Flask App Works!"