# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with the FastAPI framework, including defining routes, handling path and query parameters, and validating request bodies.

## 📝 Tasks

### 🛠️ Create Your First Endpoint

#### Description
Install FastAPI and create an application with a single `GET /` endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Create a `FastAPI` app instance in `main.py`.
- Return `{"message": "Welcome to the Book API"}` from `GET /`.
- Run with `uvicorn main:app --reload`.

### 🛠️ Read Books with Path Parameters

#### Description
Store a small in-memory list of books and add endpoints to list all books and fetch one by its id.

#### Requirements
Completed program should:

- `GET /books` returns all books.
- `GET /books/{book_id}` returns one book.
- Return a `404` error when the book does not exist.

### 🛠️ Add Books with a Request Body

#### Description
Use a Pydantic model to validate new books sent to the API.

#### Requirements
Completed program should:

- Define a `Book` model with `title` (str), `author` (str), and `year` (int).
- `POST /books` adds a new book and returns it with its new id.
- Example request body:
  ```json
  {"title": "Dune", "author": "Frank Herbert", "year": 1965}
  ```
