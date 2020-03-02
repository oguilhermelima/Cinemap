from pymongo import MongoClient

client = MongoClient('mongodb://lima:16131525@ds215370.mlab.com:15370/locais')
db = client.locais


# Carrega a collection com os locais
def place_collection():
    return db.lugares


# Carrega a collection com os usuarios
def user_collection():
    return db.users


# Carrega a collection com os locais salvos do usuário
def user_places_collection():
    return db.locais_salvos
