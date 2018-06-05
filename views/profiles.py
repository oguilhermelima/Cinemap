from flask import Blueprint, redirect, request, flash, url_for, render_template
from flask_login import login_required, current_user, logout_user
from .db_user_places import add_user_places, find_user_places, remove_user_place
from .validations import validate_edit, new_password, validate_password
from .db_users import delete_user
from .db_places import find_by_id
from .places import Places
from .maps import maps

profiles = Blueprint('profile', __name__)

# Página de perfil do usuário
@profiles.route('/perfil')
@login_required
def profile():
    places = []
    new_map=''
    # Lista todos os locais que tem o usuário atual como id
    list_places = find_user_places(current_user._id)
    if list_places.count() != 0:
        # Se a lista não está vazia, armazena na list places
        for place in list_places:
            places.append(place)
        # Cria um mapa com os locais
        new_map = maps(places)
    else:
        list_places = 0
    return render_template('profile.html', titulo="Meu Perfil", places=places, movingmap=new_map)

# Página para editar o usuário
@profiles.route('/editarusuario')
@login_required
def edit_user():
    return render_template('edit_profile.html', titulo="Perfil")

# Rota para finalizar a edição do usuario
@profiles.route('/finalizaredicao', methods=['POST', 'GET'])
@login_required
def finish_edit():
    # Recebe os dados do usuário da sessão atual
    email = current_user.email
    username = current_user._id
    # Recebe os dados do form
    new_email = request. form['email']
    new_username = request. form['usuario']
    name = request. form['nome']
    try:
        # Tenta validar os dados e retorna verdadeiro ou falso
        result = validate_edit(username, new_username, email, new_email, name)
        # Se conseguiu validar, redireciona para o perfil com mensagem de sucesso!
        if result:
            return redirect(url_for('profile.profile'))
        # Se não, retorna para a pagina de editar com as mensagens de erro
        return redirect(url_for('profile.edit_user'))    
    except:
        # Caso dê algum erro, refresh na página com as mensagens de erro
        return redirect(url_for('profile.edit_user'))

# Página para editar a senha
@profiles.route('/editarsenha')
@login_required
def edit_password():
    return render_template('edit_password.html', titulo="Perfil")

# Rota para finalizar a edição da senha
@profiles.route('/finalizarsenha', methods=['POST', 'GET'])
@login_required
def finish_password():
    # Recebe a senha digitada no form
    password = request. form["psw"]
    confirm_password = request. form["password"]
    # Verifica se as senhas são iguais
    if not validate_password(password, confirm_password):
        # Se não for, apresenta uma mensagem e atualiza a página
        return redirect(url_for('profile.edit_password'))
    # Faz hash da senha e armazena no banco
    new_password(password)
    return redirect(url_for('profile.profile'))

# Rota para deletar um usuário
@profiles.route('/deleteuser')
@login_required
def remove_user():
    # Recebe o username do usuário logado
    user = current_user._id
    try:
        # Remove o usuário do banco de dados
        delete_user(user)
        # Remove o usuário da sessão atual
        logout_user()
        # Apresenta a mensagem
        flash("Usuário removido com sucesso!")
        return redirect(url_for('signin.register'))
    except:
        flash("Não foi possível remover o usuário")
        return redirect(url_for('profile.profile'))

# Rota que salva local como favorito do usuário
@profiles.route('/salvarlocal/<string:id>/<int:qtt>/<string:cep>')
@login_required
def save_place(id, qtt, cep):
    try:
        # Busca todos os dados do local pelo id
        result = find_by_id(id)
        # Cria uma instancia com os dados do local, definindo como id o username do usuário
        place = Places(current_user._id, result['cep'], result['name'], result['street'], result['number'], 
            result['neighbor'], result['city'], result['state'], result['lat'], result['lng'], None)
        # Armazena na collection locais do usuário
        add_user_places(place.__dict__)
        flash("Local salvo com sucesso!")
    except:
    	flash("Não foi possível adicionar local")
    return redirect(url_for('index.index', qtt=qtt, cep=cep, submit="locais"))

# Rota que remove o local salvo pelo usuário
@profiles.route('/removerlocal<string:id>')
@login_required
def delete_place(id):
    try:
        # Remove o local pelo ObjectID
        remove_user_place(id)
        # Exibe mensagem de sucesso
        flash("Local removido com sucesso!")
    except:
        flash("Não foi possível remover o local")
    return redirect(url_for('profile.profile'))