# AWS Logging Test

A FastAPI application designed for testing AWS logging and deployment configurations with AWS Python Elastic Beanstalk and Aurora RDS PostgreSQL. This project provides a simple API with database connectivity for testing purposes.

## Features

-   FastAPI web application with Aurora RDS PostgreSQL database integration
-   Database test endpoints for connection testing and data manipulation
-   AWS Elastic Beanstalk Python environment deployment support
-   Interactive API documentation with Swagger UI

## Requirements

-   Python 3.8+
-   AWS Aurora RDS PostgreSQL database
-   AWS Elastic Beanstalk (for deployment)

## Setup

1. Clone the repository
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Set environment variables:

    Option 1: Using environment variables directly:

    ```
    export DB_HOST=your_db_host
    export DB_NAME=your_db_name
    export DB_USER=your_db_username
    export DB_PASSWORD=your_db_password
    ```

    Option 2: Using a .env file (recommended for local development):

    ```
    # Copy the example file
    cp .env.example .env

    # Edit the .env file with your database credentials
    nano .env  # or use your preferred text editor
    ```

## Running Locally

```
python main.py
```

The application will start on port 8000 (http://localhost:8000).

## API Documentation

FastAPI provides automatic interactive API documentation:

-   Swagger UI: http://localhost:8000/docs
-   ReDoc: http://localhost:8000/redoc

## API Endpoints

-   `/` - Home page
-   `/db/test` - Test database connection
-   `/db/info` - Get database information
-   `/db/add-users/{count}` - Add random users to the database

## Deployment

Use the included script to create a deployment package for Elastic Beanstalk:

```
./create-deploy-zip.sh
```

This will create `eb-deploy.zip` which can be uploaded to Elastic Beanstalk.
