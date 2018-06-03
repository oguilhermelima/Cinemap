from werkzeug.security import generate_password_hash
from flask import flash, request
from flask_login import current_user
from .db_users import edit_user, find_user, find_email

# Verifica se o usuario consta no banco de dados
def user_exists(username):
    # Procura o username no banco
    user = find_user(username)
    if user:
        # Se existir, retorna a mensagem e verdadeiro      
        flash("Username já cadastrado")
        return True
    return False

# Verifica se o email consta no banco de dados
def email_exists(email):
    if find_email(email):
        # Se existir, retorna a mensagem e verdadeiro
        flash("Email já cadastrado")
        return True
    return False    

# Verifica se existe algum usuario na sessão
def active_user():
    if current_user.name:
        # Se existir, retorna a mensagem e verdadeiro
        return True
    return False

# Verifica se o novo username é igual ao antigo ou se o novo usuário existe no banco
def check_actual_user(actual, new):
    if actual == new:
        # Se o username atual e o novo forem iguais, retorna verdadeiro
        return True
    elif user_exists(new):
        # Se não forem iguais, verifica no banco de dados se já existe algum usuário 
        # com o novo username
        return False
    return True

# Verifica se o novo email é igual ao antigo ou se o novo usuário existe no banco
def check_actual_email(actual, new):
    if actual == new:
        # Se o email atual e o novo forem iguais, retorna verdadeiro
        return True
    elif email_exists(new):
        # Se não forem iguais, verifica no banco de dados se já existe algum usuário 
        # com o novo username
        return False
    return True

# Valida as mudanças na edição do usuário
def validate_edit(username, new_username, email, new_email, name):
    # Verifica se o novo email existe
    result_email = check_actual_email(email, new_email)
    # Verifica se o novo username existe
    result_username = check_actual_user(username, new_username)
    # Se ambos retornarem True, os dados são alterados no banco
    if result_username and result_email:
        user = {'username' :new_username, 'name': name, 'email': new_email}
        edit_user(username, user)
        return True
    else:
        return False

# Faz o hash da nova senha e substitui no banco
def new_password(password):
    # Hash
    new = generate_password_hash(password)
    edit_user(current_user._id, {'password' :new})

# Verifica se o usuário é administrador
def is_adm():
    try:
        # Se o tipo do usuário for administrador, retorna verdadeiro
        if current_user.type == 'admin':
            return True
    except:
        return False
