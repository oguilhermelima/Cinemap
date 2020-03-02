from .collections import place_collection
from bson.objectid import ObjectId
from pymongo import GEO2D
from flask import flash


collection = place_collection()


def insert_place(place):
    try:
        collection.insert(place)
    except:
        flash("Não foi possível inserir os dados no banco")


def list_all_places():
    return [place for place in collection.find().sort('name')]


def list_places_by_user(user, qtt):
    places = [user]
    # Variavel com os termos de pesquisa no Mongo
    query = {"coordinates": {"$near": [places[0]['lat'], places[0]['lng']]}}
    # Cria um indice de busca na collection lugares
    collection.create_index([("coordinates", GEO2D)])
    query = collection.find(query).limit(qtt)
    # Busca os 10 locais mais proximos
    for place in query:
        places.append(place)
    return places


def find_by_id(place):
    try:
        return collection.find_one({'_id': ObjectId(place)})
    except:
        print("Não foi possivel encontrar local")


def find_place_by_id(id):
    try:
        return collection.find_one({'id': id})
    except:
        print("Não foi possivel encontrar local")


def update_place(place_id, place):
    collection.update({'_id': ObjectId(place_id)}, {"$set": place})


def delete_place(place_id):
    collection.remove({'_id': ObjectId(place_id)})
