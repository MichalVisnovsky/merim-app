# Merim API

A FastAPI-based application that handles menu and VAT rate data in combination with external data sources.

## Features

- Accepts and validates JSON data for menus and VAT rates
- Fetches and stores external data from a remote API periodicaly
- Combines internal and external data into a single endpoint
- Async PostgreSQL database with SQLAlchemy
- Swagger/OpenAPI documentation
- Configurable through config.ini

## Requirements

- Python 3.10+
- PostgreSQL 15+
- Docker and Docker Compose 

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running with Docker

1. Build and start the containers:
   ```bash
   docker-compose up -d
   ```


### API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Logging

Logs are written to the console and can be configured through the logging level in the configuration.
