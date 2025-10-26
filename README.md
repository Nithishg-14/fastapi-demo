# FastAPI Product Management API

A RESTful API built with FastAPI for managing product information. This project demonstrates CRUD operations for products with a PostgreSQL database.

## Features

- RESTful API endpoints for product management
- PostgreSQL database integration using SQLAlchemy ORM
- Environment variable configuration
- Docker support for easy deployment
- Input validation using Pydantic models

## Prerequisites

- Python 3.7+
- PostgreSQL database
- pip (Python package installer)
- Docker and Docker Compose (optional, for containerized setup)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-demo
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Unix or MacOS
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with the following variables:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/fastapi_demo
   APP_NAME=FastAPI Product API
   VERSION=1.0.0
   DEBUG=True
   ```
   Replace the database URL with your PostgreSQL credentials.

## Running the Application

### Development Server

1. **Start the database**
   Make sure PostgreSQL is running on your machine.

2. **Run the FastAPI development server**
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the API documentation**
   - Open your browser and go to: http://localhost:8000/docs
   - Or view the alternative documentation at: http://localhost:8000/redoc

### Using Docker

1. **Build and start the containers**
   ```bash
   docker-compose up --build
   ```

2. **Access the API**
   The API will be available at: http://localhost:8000

## API Endpoints

- `GET /` - Health check endpoint
- `GET /products` - Get all products
- `GET /products/{id}` - Get a specific product by ID
- `POST /products` - Create a new product
- `PUT /products/{id}` - Update a product
- `DELETE /products/{id}` - Delete a product

## Project Structure

```
fastapi-demo/
├── .env                    # Environment variables
├── .gitignore
├── README.md               # This file
├── database.py             # Database connection and session
├── database_models.py      # SQLAlchemy models
├── docker-compose.yml      # Docker Compose configuration
├── main.py                 # Main FastAPI application
├── models.py               # Pydantic models
└── requirement.txt         # Project dependencies
```

## Technologies Used

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **PostgreSQL** - Powerful, open-source relational database
- **Docker** - Containerization platform
- **Python-dotenv** - Environment variable management

## License

This project is open-source and available under the [MIT License](LICENSE).