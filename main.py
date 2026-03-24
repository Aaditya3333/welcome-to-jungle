''''from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import engine, SessionLocal

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all todos
@app.get("/todos", response_model=list[schemas.TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_all_todos(db)

# GET todo by ID
@app.get("/todos/{todo_id}", response_model=schemas.TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# POST create todo
@app.post("/todos", response_model=schemas.TodoResponse)
def create(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

# PUT update todo
@app.put("/todos/{todo_id}", response_model=schemas.TodoResponse)
def update(todo_id: int, updated: schemas.TodoCreate, db: Session = Depends(get_db)):
    todo = crud.update_todo(db, todo_id, updated)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# DELETE todo
@app.delete("/todos/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.delete_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"} '''

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Item(BaseModel):
    name: str
    price: int

class Movie(BaseModel):
    name: str
    rating: float

@app.post("/movies")
def add_movie(movie: Movie):
    return {"movie": movie}

@app.get("/")
def home():
    return {"message": "Welcome Home"}

@app.get("/about")
def about():
    return {"message": "This is About Page"}

@app.get("/contact")
def contact():
    return {"message": "Contact us here"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/student/{name}/{age}")
def get_student(name: str, age: int):
    return {"name": name, "age": age}

@app.get("/product/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id}

@app.get("/items")
def get_items(name: str, price: int):
    return {"name": name, "price": price}

@app.get("/products")
def get_products(name: str = "unknown", price: int = 0):
    return {"name": name, "price": price}



@app.get("/search")
def search_item(name: Optional[str] = None):
    return {"search": name}

@app.get("/filter")
def filter_items(name: str, price: int, brand: str):
    return {
        "name": name,
        "price": price,
        "brand": brand
    }

@app.get("/movies")
def get_movies(name:str, rating:float):
    return {"name":name, "rating":rating}

@app.post("/create")
def create_item(name: str, price: int):
    return {
        "message": "Item created",
        "name": name,
        "price": price
    }

@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "data":item
    }

print("Hello World")