from .collections import user_places_collection as up_collection
from bson.objectid import ObjectId
from flask import flash

# Create
# Insere locais na collection user_places 
def add_user_places(place):
    # Carrega a collection de locais de determinado usuário
    collection = up_collection()
    try:
        # Insere o local na collection
        collection.insert(place)
    except:
        flash("Não foi possível salvar este local. Local já está na lista.")

# Read
# Procura locais na collection user_places pelo id do usuário
def find_user_places(username):
    # Carrega a collection de locais de determinado usuário
    collection = up_collection()
    try:
        # Busca os locais na colection pelo id
        user_places = collection.find({'id': username}).sort('name')
        return user_places
    except:
        print("Não foi possivel encontrar locais desse usuário")

# Delete
# Remove local na collection user_places pelo ObjectIDd do local
def remove_user_place(id):
    # Carrega a collection de locais de determinado usuário
    collection = up_collection()
    try:
        # Remove o local da collection
        collection.remove({'_id': ObjectId(id) })
    except:
        print("Não foi possível remover o local")