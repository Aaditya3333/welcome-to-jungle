from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

movies = []

class Movie(BaseModel):
    id: int
    name: str
    rating: float

#creating post
@app.post("/movies")
def add_movies(movie: Movie):
    movies.append(movie.dict())
    return {"message": "Movie added", "data": movie}

#reading get

@app.get('/movies')
def get_movies():
    return movies

#single movie get
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return {"error": "Movie not found"}

#updating put
@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, updated_movie: Movie):
    for index, movie in enumerate(movies):
        if movie["id"] == movie_id:
            movies[index] = updated_movie.dict()
            return {"message": "Movie updated", "data": update_movie}
        return {"error": "Movie not found"}
    
#deleting the data
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    for index, movie in enumerate(movies):
        if movie["id"] == movie_id:
            deleted = movies.pop(index)
            return {"message": "Movie deleted", "data": deleted}
        return {"error": "Movie not found"}