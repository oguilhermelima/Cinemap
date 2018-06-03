from .collections import user_places_collection
from .collections import user_collection

# Create
# Insere usuarios no banco
def add_user(user):
    # Carrega a collection de usuários
    collection = user_collection()
    try:
        # Insere os dados na collection
        collection.insert(user)
    except:
        print ("Não foi possível inserir os dados no banco")

# Read All
# Devolve todos os usuários do banco de dados
def return_users():
    # Carrega a collection de usuários
    collection = user_collection()
    users = []
    try:
        # Busca o usuário e retorna todos os dados 
        user = collection.find().sort('_id')
        return user
    except:
        print ("Não foi possível encontrar usuários") 

# Read one
# Pesquisa 1(um) usuario no banco pelo username
def find_user(username):
    # Carrega a collection de usuários
    collection = user_collection()
    try:
        # Busca o usuário e retorna todos os dados 
        user = collection.find_one({'_id': username })
        return user
    except:
        print ("Não foi possível encontrar usuários") 

# Find one
# Pesquisa 1(um) usuario no banco pelo email
def find_email(email):
    # Carrega a collection de usuários
    collection = user_collection()
    try:
        # Busca o usuário e retorna todos os dados 
        e_mail = collection.find_one({'email': email })
        return e_mail
    except:
        print ("Não foi possível encontrar usuários")  

# Update one
def edit_user(id, user):
    # Carrega a collection de locais
    collection = user_collection()
    try:
        # Faz o update do usuário
        collection.update({'_id': id}, {"$set": user})
    except:
        print("Não foi possivel editar usuário")

# Delete
def delete_user(username):
    # Carrega a collection de usuários
    collection = user_collection()
    # Carrega a collection locais do usuário
    collection2 = user_places_collection()
    try:
        # Remove o usuário da collection users
        collection.remove({'_id': username})
        # Remove todos os locais com id igual ao username do usuário deletado
        collection2.remove({'id': username})
    except:
        print("Não foi possivel deletar o usuário")

