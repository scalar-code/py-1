from fastapi import FastAPI, HTTPException
from typing import List
import database
import model
from model import Book, BookCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the books CRUD API"}

@app.post("/books/", response_model=Book)
def create_book(book: BookCreate):
    """Creates a new book in the database."""
    book_id = database.create_book(book)
    return model.book(id=book_id, **book.dict())

@app.get("/books/", response_model=List[Book])
def read_books():
    """Retrieves all books from the database."""
    return database.read_books()

@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    """Retrieves a single book by its ID."""
    book = database.read_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="book not found")
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate):
    """Updates an existing book in the database."""
    updated = database.update_book(book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="book not found")
    return model.book(id=book_id, **book.dict())

@app.delete("/books/{book_id}", response_model=dict)
def delete_book(book_id: int):
    """Deletes a book from the database by its ID."""
    deleted = database.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="book not found")
    return {"message": "book deleted successfully"}