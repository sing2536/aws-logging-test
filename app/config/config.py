"""Configuration settings for the application."""
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Database configuration
# Get database connection details from environment variables
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

# Construct the database URI
DB_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

