from flask import Blueprint, redirect, request, flash, url_for, render_template
from flask_login import login_required, current_user, logout_user
from database.db_user_places import add_user_place, find_user_places, remove_user_place
from util.validations import update_subscription, new_password, validate_password
from database.db_users import delete_user
from database.db_places import find_by_id
from file.models import Places
from service.maps_service import create_map_pin

profiles = Blueprint('profile', __name__)


@profiles.route('/perfil')
@login_required
def profile():
    list_places = find_user_places(current_user._id)
    pins = create_map_pin([place for place in list_places]) if list_places.count() != 0 else ''
    return render_template('profile.html', titulo="Meu Perfil", places=[], movingmap=pins)


@profiles.route('/editarusuario')
@login_required
def edit_account():
    return render_template('edit_profile.html', titulo="Perfil")


@profiles.route('/finalizaredicao', methods=['POST', 'GET'])
@login_required
def finish_edit():
    email = current_user.email
    username = current_user._id
    new_email = request.form['email']
    name = request.form['nome']
    try:
        result = update_subscription(username, email, new_email, name)
        if result:
            flash("Dados alterados com sucesso!")
            return redirect(url_for('profile.profile'))
        flash("E-mail inválido")
        return redirect(url_for('profile.edit_account'))
    except:
        return redirect(url_for('profile.edit_account'))


@profiles.route('/editarsenha')
@login_required
def edit_password():
    return render_template('edit_password.html', titulo="Perfil")


@profiles.route('/finalizarsenha', methods=['POST', 'GET'])
@login_required
def finish_password():
    password = request.form["psw"]
    confirm_password = request.form["password"]
    if not validate_password(password, confirm_password):
        # Se não for, apresenta uma mensagem e atualiza a página
        return redirect(url_for('profile.edit_password'))
    # Faz hash da senha e armazena no banco
    new_password(password)
    return redirect(url_for('profile.profile'))


# Rota para deletar um usuário
@profiles.route('/deleteuser')
@login_required
def delete_account():
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
@profiles.route('/salvarlocal/<string:id>/<string:cep>/<int:qtt>')
@login_required
def add_place_to_bookmarks(id, cep, qtt):
    try:
        # Busca todos os dados do local pelo id
        result = find_by_id(id)
        # Cria uma instancia com os dados do local, definindo como id o username do usuário
        place = Places(current_user._id, result['cep'], result['name'], result['street'], result['number'],
                       result['neighbor'], result['city'], result['state'], result['lat'], result['lng'], None)
        # Armazena na collection locais do usuário
        add_user_place(place.__dict__)
        flash("Local salvo com sucesso!")
    except:
        flash("Não foi possível adicionar local")
    return redirect(url_for('index.home', qtt=qtt, cep=cep, submit="locais"))


# Rota que remove o local salvo pelo usuário
@profiles.route('/removerlocal<string:id>')
@login_required
def delete_place_from_bookmarks(id):
    try:
        # Remove o local pelo ObjectID
        remove_user_place(id)
        # Exibe mensagem de sucesso
        flash("Local removido com sucesso!")
    except:
        flash("Não foi possível remover o local")
    return redirect(url_for('profile.profile'))
