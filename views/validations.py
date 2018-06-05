from werkzeug.security import generate_password_hash
from flask import flash
from flask_login import current_user
from pycep_correios import consultar_cep # Api correios que recebe o CEP e retorna o Endereço
from .db_users import edit_user, find_user, find_email

# Verifica se existe de fato um endereço para o 
def check_cep(cep):
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
    if len(username)<5:
        # Se o tamanho do username for menor 5 retorna mensagem de erro
        return True
    # Procura o username no banco
    user = find_user(username)
    if user:
        # Se existir, retorna verdadeiro      
        return True
    return False

# Verifica se o email consta no banco de dados
def email_exists(email):
    if find_email(email):
        # Se existir, retorna verdadeiro
        return True
    return False    

# Valida o email e username do novo usuário    
def validate_username_email(user,email):
    # Retorna se o usuário já existe no banco
    user_validate = user_exists(user)
    # Retorna se o email já existe no banco
    email_validate = email_exists(email)
    # Se o username já existe
    if user_validate:
        # Também verifica se o email existe
        if email_validate:
            # Retorna uma mensagem de erro
            flash("Username e e-mail inválidos")
            return False
        flash("Username inválido")
        return False
    # Se username for valido e o email já existir
    elif email_validate:
        flash("Email inválido")
        return False
    # Se nenhum dos dois existir, retorna falso
    return True

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

# Termina a validação do novo usuário
def validate_user(username, email, password, confirm_password):
    # Verifica se o usuario e email já constam no banco de dados
    if not validate_username_email(username, email):
        return False
    # Se validou o email, tenta validar a senha
    elif not validate_password(password, confirm_password):
        return False
    # Se ambos forem válidados, retorna true
    return True    

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
        # Cria um dict para armazenar no mongo
        user = {'username' :new_username, 'name': name, 'email': new_email}
        # Faz update com o dict
        edit_user(username, user)
        # Apresenta mensagem e retorna verdadeiro
        flash("Dados alterados com sucesso!")
        return True
    elif result_username:
        # Se o username estiver certo e email inválido
        flash("E-mail inválido")
        return False
    elif result_email:
        # Se o email estiver válido e o usuário não
        flash("Username inválido")
        return False
    else:
        # Se username e e-mail estiverem incorretos
        flash("Username e e-mail inválidos")
        return False

# Faz o hash da nova senha e substitui no banco
def new_password(password):
    # Hash
    new = generate_password_hash(password, method='sha256')
    # Atualiza a senha no banco
    edit_user(current_user._id, {'password' :new})
    flash("Senha alterada com sucesso!")

# Verifica se o usuário é administrador
def is_adm():
    try:
        # Se o tipo do usuário for administrador, retorna verdadeiro
        if current_user.type == 'admin':
            return True
    except:
        return False