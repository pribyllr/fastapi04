# FastAPI04 - Blog Management API

A RESTful API built with FastAPI for managing blog articles and comments. This project demonstrates SQLAlchemy ORM relationships, FastAPI routing, dependency injection, and PostgreSQL database integration.

## 📋 Overview

FastAPI04 is a content management API that allows you to:
- Retrieve all articles with their associated comments
- View specific articles by ID with comments
- Access comments for specific articles
- Manage a one-to-many relationship between articles and comments

## 🛠️ Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)
- Virtual environment tool (venv)

## 📦 Installation

### 1. Clone/Access the Project
```bash
cd FastAPI04
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.\.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

## ⚙️ Configuration

### 1. Set Up Environment Variables

Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```

### 2. Configure `.env` File

Edit `.env` with your PostgreSQL credentials:
```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=your_password
```

### 3. Ensure PostgreSQL is Running

Make sure PostgreSQL service is running on your system:

**Windows (via Services):** Start PostgreSQL service
**Linux/macOS:** 
```bash
# macOS with Homebrew
brew services start postgresql

# Linux (systemd)
sudo systemctl start postgresql
```

### 4. Create Database

Create the `fastapi_week4` database:
```bash
psql -U postgres -c "CREATE DATABASE fastapi_week4;"
```

Or via PostgreSQL client:
1. Open pgAdmin or psql
2. Create a new database named `fastapi_week4`

## 🚀 Running the Server

Activate the virtual environment and start the development server:

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`

### API Documentation

- **Interactive API Docs (Swagger UI):** `http://127.0.0.1:8000/docs`
- **Alternative Docs (ReDoc):** `http://127.0.0.1:8000/redoc`

## 📚 API Endpoints

### Health Check

**GET `/`**
```
Description: Verify API is running
Response: 200 OK
{
  "message": "FastAPI is running!"
}
```

### Articles

**GET `/articles/`**
```
Description: Retrieve all articles with their comments
Response: 200 OK
[
  {
    "id": 1,
    "title": "Article 1",
    "comments": [
      {
        "id": 1,
        "content": "Great article!",
        "article_id": 1
      },
      {
        "id": 2,
        "content": "Thanks for sharing",
        "article_id": 1
      }
    ]
  },
  ...
]
```

**GET `/articles/{article_id}`**
```
Description: Retrieve a specific article by ID with all its comments
URL Parameter: article_id (integer)
Response: 200 OK
{
  "id": 1,
  "title": "Article 1",
  "comments": [
    {
      "id": 1,
      "content": "Great article!",
      "article_id": 1
    },
    {
      "id": 2,
      "content": "Thanks for sharing",
      "article_id": 1
    }
  ]
}
```

### Comments

**GET `/comments/article/{article_id}`**
```
Description: Retrieve all comments for a specific article
URL Parameter: article_id (integer)
Response: 200 OK
[
  {
    "id": 1,
    "content": "Great article!",
    "article_id": 1
  },
  {
    "id": 2,
    "content": "Thanks for sharing",
    "article_id": 1
  }
]
```

## 💻 Usage Examples

### Using cURL

**Get all articles:**
```bash
curl http://127.0.0.1:8000/articles/
```

**Get specific article:**
```bash
curl http://127.0.0.1:8000/articles/1
```

**Get comments for article:**
```bash
curl http://127.0.0.1:8000/comments/article/1
```

### Using Python Requests

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# Get all articles
response = requests.get(f"{BASE_URL}/articles/")
articles = response.json()
print(articles)

# Get specific article
response = requests.get(f"{BASE_URL}/articles/1")
article = response.json()
print(article)

# Get comments for article
response = requests.get(f"{BASE_URL}/comments/article/1")
comments = response.json()
print(comments)
```

## 📁 Project Structure

```
FastAPI04/
├── main.py                 # Application entry point and routes
├── database.py             # Database configuration and session management
├── .env                    # Environment variables (local)
├── .env.example            # Environment variables template
├── README.md               # This file
├── dependencies/
│   └── auth.py            # Authentication module (placeholder for future use)
├── models/
│   ├── base.py            # SQLAlchemy declarative base
│   ├── article.py         # Article model (ORM)
│   └── comment.py         # Comment model (ORM)
└── routers/
    ├── articles.py        # Articles API routes
    └── comments.py        # Comments API routes
```

## 🗄️ Database Models

### Article Model
- **id** (Integer, Primary Key): Unique article identifier
- **title** (String, Indexed): Article title
- **comments** (Relationship): One-to-many relationship with comments

### Comment Model
- **id** (Integer, Primary Key): Unique comment identifier
- **content** (String, Indexed): Comment text
- **article_id** (Integer, Foreign Key): Reference to parent article

## 📝 Development Notes

- Tables are automatically created on application startup if they don't exist
- Sample data is loaded on first run demonstrating the article-comment relationship
- Uses SQLAlchemy ORM for database abstraction and query building

### SQLAlchemy Base Configuration: DeclarativeBase vs declarative_base

This project uses **`DeclarativeBase`** class for creating the declarative base. Here's the difference:

**Legacy approach (`declarative_base`):**
```python
from sqlalchemy.orm import declarative_base
Base = declarative_base()
```
- Function-based approach (deprecated in SQLAlchemy 2.0+)
- Returns an instance of the declarative base
- Less type-safe

**Modern approach (`DeclarativeBase`):**
```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```
- Class-based approach (recommended for SQLAlchemy 2.0+)
- More explicit and maintainable
- Allows customization through inheritance
- Improved integration with Pydantic and type checkers

**Benefits of using `DeclarativeBase`:**
- ✅ Full type annotation support
- ✅ More Pythonic and object-oriented
- ✅ Forward-compatible with SQLAlchemy 2.0+
- ✅ Easier to extend with custom functionality

All models in this project inherit from the `DeclarativeBase` subclass defined in [models/base.py](models/base.py), providing a consistent and modern ORM foundation.
