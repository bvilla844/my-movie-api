from fastapi import FastAPI
from config.database import engine,base
from middlewares.error_handle import Errorhandle
from routers.movie import movie_router
from routers.user import user_router


app= FastAPI()
app.title = 'Mi aplicacion con fastAPI'
app.version = '0.0.20'

app.add_middleware(Errorhandle)
app.include_router(movie_router)
app.include_router(user_router)
base.metadata.create_all(bind=engine)

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "AVATAR nos lleva a un mundo situado más allá de la imaginación, en donde un recién llegado de la Tierra se embarca en una aventura épica, llegando a luchar, al final, por salvar el extraño mundo al que ha aprendido a llamar su hogar. ",
        "year": "2009",
        "rating": 7.8,
        "category":"Accion"
    },
    {

        "id": 2,
        "title": "Avatar",
        "overview": "AVATAR nos lleva a un mundo situado más allá de la imaginación, en donde un recién llegado de la Tierra se embarca en una aventura épica, llegando a luchar, al final, por salvar el extraño mundo al que ha aprendido a llamar su hogar. ",
        "year": "2009",
        "rating": 7.8,
        "category":"Accion"
    }
]

    

