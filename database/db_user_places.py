from .collections import user_places_collection as up_collection
from bson.objectid import ObjectId

collection = up_collection()


def add_user_place(place):
    try:
        collection.insert(place)
    except:
        print("Não foi possível salvar este local. Local já está na lista.")


def find_user_places(username):
    return collection.find({'id': username}).sort('name')


def remove_user_place(place_id):
    try:
        collection.remove({'_id': ObjectId(place_id)})
    except:
        print("Não foi possível remover o local")


def remove_all_user_places(username):
    try:
        # Remove todos os locais com id igual ao username do usuário deletado
        collection.remove({'id': username})
    except:
        print("Não foi possível remover locais do usuário")
