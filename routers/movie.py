from fastapi import APIRouter
from fastapi import Path, Query,Depends
from fastapi.responses import HTMLResponse,JSONResponse
from config.database import sesion
from model.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from esquemas.movie import Movie
movie_router= APIRouter()

class Config:
        schema_extra= {
            "example":{
                "id":1,
                "title":"mi pelicula",
                "overview":"decripsion de la pelicula",
                "year":2020,
                "rating":5,
                "category":"accion"
            }
            }
            
@movie_router.get('/', tags=['home'])
def message():
    return HTMLResponse ('<h1>hello worls</h1>')

@movie_router.get('/movies', tags=['movies'], response_model=list[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> list[Movie]:
    db = sesion()
    result= +MovieService(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1,le=2000)) -> Movie:
    db = sesion()
    result= MovieService(db).get_movie(id)
    result= db.query(MovieModel).filter(MovieModel.id== id).first()
    if not result:
        return JSONResponse(status_code=404, content={"mensaje":"no se encontro"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/', tags=['movies'], response_model=list[Movie])
def get_movies_by_category(category: str = Query (min_length=5, max_length=15)) -> Movie:
    db = sesion()
    result=  MovieService(db).get_movies_by_category(category)
    return JSONResponse (status_code=200, content=jsonable_encoder(result))

@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201) 
def create_movie (movie: Movie) -> dict:
    db = sesion()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201,content={'message':'se registro la pelicula'})

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int , movie: Movie) -> dict:
    db = sesion()
    result= MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"mensaje":"no se encontro"})
    MovieService(db).update_movie(id,movie)
    return JSONResponse(status_code=404 , content={'message':'se ha modificado la pelicula'})

@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    db = sesion()
    result : MovieModel= db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"mensaje":"no se encontro"})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200,content={'message':'se ha eliminado la pelicula'})

def create_movie(self,movie: Movie):
    new_movie=MovieModel(**movie.dict())
    self.db.add(new_movie)
    self.db.commit()
    return

