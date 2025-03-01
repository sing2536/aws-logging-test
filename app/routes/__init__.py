"""Routes initialization."""

def init_routes(app):
    """Register all blueprints/routes with the app."""
    # Import the blueprints
    from app.routes.main import main_bp
    from app.routes.db import db_bp
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(db_bp, url_prefix='/db') 