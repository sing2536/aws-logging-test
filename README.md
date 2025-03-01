# AWS Logging Test

A Flask application designed for testing AWS logging and deployment configurations with AWS Python Elastic Beanstalk and Aurora RDS PostgreSQL. This project provides a simple API with database connectivity for testing purposes.

## Features

-   Flask web application with Aurora RDS PostgreSQL database integration
-   Database test endpoints for connection testing and data manipulation
-   AWS Elastic Beanstalk Python environment deployment support

## Requirements

-   Python 3.x
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

## API Endpoints

-   `/` - Home page
-   `/test` - Test database connection
-   `/info` - Get database information
-   `/add-users/<count>` - Add random users to the database

## Deployment

Use the included script to create a deployment package for Elastic Beanstalk:

```
./create-deploy-zip.sh
```

This will create `eb-deploy.zip` which can be uploaded to Elastic Beanstalk.
