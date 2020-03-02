from werkzeug.security import generate_password_hash
from flask import flash
from flask_login import current_user
from pycep_correios import consultar_cep
from database.db_users import update_user, find_user, find_user_by_email


# Verifica se existe de fato um endereço para o CEP que vai ser salvo
def valid_cep(cep):
    try:
        # Recebe o endereço completo do CEP
        check_cep = consultar_cep(cep)
        # Se existir um CEP no endereço do retorno, retorna verdadeiro
        if check_cep['cep']:
            return True
    except:
        # Se não existir, retorna falso e uma mensagem
        flash("CEP inválido, tente novamente")
        return False


# Verifica se o usuario consta no banco de dados
def user_exists(username):
    user = find_user(username)
    return True if user else False


# Verifica se o email consta no banco de dados
def email_exists(email):
    return True if find_user_by_email(email) else False


# Valida a senha
def validate_password(password, confirm_password):
    # Se as senhas digitadas forem iguais
    if password == confirm_password:
        # Retorna verdadeiro
        return True
    else:
        # Se não, retorna falso e uma mensagem
        flash("Senhas não são iguais")
        return False


def valid_user(username, email, password, confirm_password):
    user_is_valid = find_user(username)
    email_is_valid = email_exists(email)
    if user_is_valid:
        if email_is_valid:
            flash("Username e e-mail inválidos")
            return False
        flash("Username inválido")
        return False
    elif email_is_valid:
        flash("Email inválido")
        return False
    elif not validate_password(password, confirm_password):
        return False
    return True


# Verifica se existe algum usuario na sessão
def active_user():
    if current_user.name:
        # Se existir, retorna a mensagem e verdadeiro
        return True
    return False


# Valida as mudanças na edição do usuário
def update_subscription(username, email, new_email, name):
    if email == new_email or email_exists(new_email):
        user = {'name': name, 'email': new_email}
        update_user(username, user)

        return True
    else:
        flash("E-mail inválido")
        return False


# Faz o hash da nova senha e substitui no banco
def new_password(password):
    # Hash
    new = generate_password_hash(password, method='sha256')
    # Atualiza a senha no banco
    update_user(current_user._id, {'password': new})
    flash("Senha alterada com sucesso!")
