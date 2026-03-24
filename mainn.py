from fastapi import FastAPI
from models import Book # Importing the class we just made

app = FastAPI()

# Temporary "Database"
BOOKS = [
    Book(id=1, title="Python Deep Dive", author="Guido", description="Advanced Python", rating=5),
    Book(id=2, title="FastAPI Essentials", author="Tiangolo", description="Web stuff", rating=4),
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request: Book):
    BOOKS.append(book_request)
    return {"message": "Book created successfully"}