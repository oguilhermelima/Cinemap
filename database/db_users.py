from .collections import user_places_collection
from .collections import user_collection

collection = user_collection()


def add_user(user):
    try:
        collection.insert(user)
    except:
        print("Não foi possível inserir os dados no banco")


def list_all_users():
    query = collection.find()
    return query.sort('_id') if query else query


def find_user(username):
    try:
        return collection.find_one({'_id': username})
    except:
        print("Não foi possível encontrar usuários")


def find_user_by_email(email):
    try:
        return collection.find_one({'email': email})
    except:
        print("Não foi possível encontrar usuários")


def update_user(user_id, user):
    try:
        collection.update({'_id': user_id}, {"$set": user})
    except:
        print("Não foi possivel editar usuário")


def delete_user(username):
    # Carrega a collection locais do usuário
    collection2 = user_places_collection()
    try:
        # Remove o usuário da collection users
        collection.remove({'_id': username})
        # Remove todos os locais com id igual ao username do usuário deletado
        collection2.remove({'id': username})
    except:
        print("Não foi possivel deletar o usuário")

