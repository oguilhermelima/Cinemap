from .collections import place_collection
from bson.objectid import ObjectId
from pymongo import GEO2D
from flask import flash

# Create
# Insere os locais no banco 
def insert_places(place):
    # Carrega a collection de locais
    collection = place_collection()
    try:
        # Insere os dados na collection
        collection.insert(place)
    except:
        flash("Não foi possível inserir os dados no banco")

# Read all
# Procura os locais no banco para atualizar a lista e o mapa
def find_places(user, qtt):
    # Carrega a collection de locais
    collection = place_collection()
    # Cria um array que irá armazenar os pontos
    places = []
    if user:
        places.append(user)
        # Variavel com os termos de pesquisa no Mongo
        query = {"coordinates":{"$near": [places[0]['lat'], places[0]['lng']]}}
        # Cria um indice de busca na collection lugares
        collection.create_index([("coordinates", GEO2D)])
        # Busca os 10 locais mais proximos. 
        for place in collection.find(query).limit(qtt):
            places.append(place)
        return places
    # Busca todos os usuários no banco e ordena por nome
    for place in collection.find().sort('name'):
        places.append(place)
    return places

# Read one
# Find por _ID
def find_by_id(place):
    # Carrega a collection de locais
    collection = place_collection()
    try:
        # Busca o id na collection
        place_id = collection.find_one({'_id': ObjectId(place) })
        return place_id
    except:
        print("Não foi possivel encontrar local")

# Read one
# Find por ID
def find_byid(id):
    # Carrega a collection de locais
    collection = place_collection()
    try:
        # Busca o id na collection
        place_id = collection.find_one({'id': id})
        return place_id
    except:
        print("Não foi possivel encontrar local")

# Update
def edit_place(place_id, place):
    # Carrega a collection de locais
    collection = place_collection()
    try:
        # Faz update com os dados digitados
        collection.update({'_id': ObjectId(place_id) }, {"$set": place})
    except:
        flash("Não foi possivel atualizar")

# Delete
# Deleta um local do banco recebendo o id
def remove_place(id):
    # Carrega a collection de locais
    collection = place_collection()
    try:
        # Remove o local da collection
        collection.remove({'_id': ObjectId(id) })
    except:
        flash("Não foi possível deletar o local")