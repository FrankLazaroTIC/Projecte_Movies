from db.clientMD import client
from typing import Union
from fastapi import FastAPI
from db import movieDB
from model.film import Films
from fastapi import Path
from bson import ObjectId
app = FastAPI()

# GET - Retorna les pel·lícules
@app.get("/films")
def getMovies():
    client()
    data= movieDB.consultaMovies()
    return data

# GET - Retorna la pel·lícula per id
@app.get("/film/{id}")
def getMovieById(id: str = Path(...)):
    client()
    data = movieDB.consultaMoviesById(id)
    return data

# POST - Afegim una pel·lícula a la BBDD
@app.post("/film/")
def createFilm(film: Films):
    client()
    data= movieDB.createMovie(film)
    return data

# PUT - Modifiquem una pel·lícula de la BBDD
@app.put("/film/{id}")
def updateMovie(id,film: Films):
    client()
    data= movieDB.updateMovie(id,film)
    return data

# DELTE - Borrem una pel·lícula de la BBDD
@app.delete("/film/{id}")
def deleteMovie(id):
    client()
    data=movieDB.deleteMovie(id)
    return data


##########################################
##########################################
######### CONSULTES AVANÇADES ############
##########################################
##########################################

#GET - Consulta per filtrar per genere
@app.get("/filmsGenere")
def getMoviesG(genre: str = "Drama"):
    client()
    data= movieDB.consultaGen(genre)
    return data

#GET - Consulta per ordenar la taula per title de manera ascendent
@app.get("/filmsOrder")
def getMoviesTitle(field: str = "title", order: str = "asc"):
    client()
    # Convertir el parámetro de orden a la orden de ordenamiento de MongoDB
    mongo_order = 1 if order == "asc" else -1
    data = movieDB.consultaOrder(field, mongo_order)
    return data

#GET - Consulta que ens retornara nomes les 10 primeres 
@app.get("/filmsLimit")
def consultaLimitMovies(limit: int = "10"):
    client()
    data = movieDB.consultaLimit(limit)
    return data