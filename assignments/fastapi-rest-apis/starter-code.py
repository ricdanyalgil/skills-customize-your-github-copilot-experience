from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
]


class Book(BaseModel):
    title: str
    author: str
    year: int


@app.get("/")
def root():
    # TODO: return a welcome message
    pass

# TODO: add GET /books, GET /books/{book_id}, and POST /books
