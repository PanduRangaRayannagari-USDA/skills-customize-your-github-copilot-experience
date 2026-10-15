from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Book Catalog API")


class Book(BaseModel):
    """A book returned by the API."""

    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int


class BookCreate(BaseModel):
    """The fields a client sends when creating a book."""

    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int


books: list[Book] = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", year=1937),
]


@app.get("/")
def read_root() -> dict[str, str]:
    # TODO: Return a message confirming that the API is running.
    return {"message": "TODO"}


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    # TODO: Return all books.
    return []


@app.post("/books", response_model=Book, status_code=201)
def create_book(book_data: BookCreate) -> Book:
    # TODO: Assign the next available ID, create a Book, save it, and return it.
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    # TODO: Find and return the requested book, or raise an HTTP 404 error.
    raise NotImplementedError
