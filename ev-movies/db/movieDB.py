from db.clientMD import client
from bson.objectid  import ObjectId
from datetime import datetime
import json
from model import film

def films_schema(films):
    return [film_schema(film) for film in films]

def film_schema(film):
    return {
        "id": str(film["_id"]),
        "title": film["title"],
        "director": film["director"],
        "year": film["year"],
        "genre": film["genre"],
        "rating": film["rating"],
        "country": film["country"],
    }
    
def consultaMovies():
    try:    
        db = client()
        data=db.films.find()
        result = films_schema(data)
        return result
    except Exception as e:
        return f'Error amb la consulta {e}'

def consultaMoviesById(id):
    try:    
        db = client()
        data = db.films.find_one({"_id": ObjectId(id)})
        return film_schema(data)
    except Exception as e:
        return f'Error al consultar la película por ID: {e}'  

def createMovie(film):
    try:    
        db = client()
        data={
            "title": film.title,
            "director": film.director,
            "year": film.year,
            "genre": film.genre,
            "rating": film.rating,
            "country": film.country,
            "created_at": datetime.now(),
            "update_at": datetime.now()
        }
        id = db.films.insert_one(data).inserted_id
        return "Insertado KEK"
    except Exception as e:
        return f'Error amb la consulta {e}'

def deleteMovie(id):
    try:
        db = client()
        db.films.delete_one({"_id" : ObjectId(id)})
        return " Movie has been deleted o7 " 
    except Exception as e:
        return f'Error conexió {e}'

def updateMovie(id, film):
    try:
        db = client()
        now = datetime.now()
        data={
            "title": film.title,
            "director": film.director,
            "year": film.year,
            "genre": film.genre,
            "rating": film.rating,
            "country": film.country,
            "created_at": datetime.now(),
            "update_at": datetime.now()
        }
        id=db.films.update_one({"_id" : ObjectId(id)}, {"$set": data})
        return "Movie Updated o7 "
    except Exception as e:

        return f'Error conexió {e}'
    
##########################################
##########################################
######### CONSULTES AVANÇADES ############
##########################################
##########################################


def consultaGen(gen):
    try:    
        db = client()
        data=db.films.find({"genre": gen})
        result = films_schema(data)
        return result
    except Exception as e:
        return f'Error amb la consulta {e}'
    
def consultaOrder(field, order):
    try:    
        db = client()
        data=db.films.find().sort(field, order)
        result = films_schema(data)
        return result
    except Exception as e:
        return f'Error amb la consulta {e}'
    
def consultaLimit(limit):
    try:    
        db = client()
        data=db.films.find().limit(limit)
        result = films_schema(data)
        return result
    except Exception as e:
        return f'Error amb la consulta {e}'
    
    