'''from sqlalchemy import Column, Integer, String
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)'''

from pydantic import BaseModel, Field
from typing import Optional

class Book(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6) # Rating between 0-5

    # This provides an example in your /docs automatically!
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "Computer Science",
                "author": "FastAPI Master",
                "description": "A great book to learn coding",
                "rating": 5
            }
        }
    }

