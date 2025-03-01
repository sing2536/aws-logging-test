"""Main application entry point."""
from app import create_app

# Create the application instance
app = create_app()

if __name__ == "__main__":
    app.run(port=8000, debug=True)