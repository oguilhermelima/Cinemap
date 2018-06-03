from pymongo import MongoClient

def database():
    # Cria o cliente com autenticação no MLab
    client = MongoClient('mongodb://lima:16131525@ds215370.mlab.com:15370/locais')
    # Retorna o banco de locais
    db = client.locais
    return db    

################# PLACES #################
# Carrega a collection com os locais
def place_collection():
    # Recebe o banco de dados
    db = database()
    # Retorna a collection lugares
    collection = db.lugares

    return collection

################# USERS #################
# Carrega a collection com os usuarios
def user_collection():
    # Recebe o banco de dados
    db = database()
    # Retorna a collection usuarios
    collection = db.users 

    return collection 

################# SAVED PLACES #################
# Carrega a collection com os locais salvos do usuário
def user_places_collection():
    # Recebe o banco de dados
    db = database()
    # Retorna a collection usuarios
    collection = db.locais_salvos

    return collection
