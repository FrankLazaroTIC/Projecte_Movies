from pymongo import MongoClient

def client():
    try:
        server = "mongodb://localhost:27017/"
        return MongoClient(server).FrankDB
    except Exception as e:
        result = {"status": -1,"error":f'{e}'}
        
