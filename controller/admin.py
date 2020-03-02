from flask import Blueprint, request, redirect, flash, render_template, url_for
from database.db_places import insert_place, find_by_id, list_all_places, update_place, delete_place
from database.db_users import list_all_users, delete_user
from service.maps_service import get_coordinates
from util.decorators import admin_route
from util.validations import valid_cep
from file.modelsVO import PlaceVO
from file.models import Places


administrator = Blueprint('administration', __name__)


@administrator.route('/admin')
@admin_route
def dashboard():
    return render_template('admin/dashboard.html', titulo="Dashboard", imagem='imgs/administration.jpg')


@administrator.route('/admin/locais')
@admin_route
def places():
    return render_template('admin/places.html', titulo="Locais", imagem='imgs/add_place.jpg')


@administrator.route('/admin/locais/novolocal')
@admin_route
def add_place():
    return render_template('admin/add_place.html', titulo='Novo local', imagem='imgs/add_place.jpg')


@administrator.route('/criar', methods=['POST', ])
@admin_route
def create_place():
    try:
        place_form = PlaceVO(request.form)
        if not valid_cep(place_form.cep):
            return redirect(url_for('administration.new_place'))

        coordinates = get_coordinates(place_form.to_string())
        id_place = (place_form.name.replace(" ", "") + str(place_form.cep) + str(place_form.number))

        place = Places(id_place, place_form.cep, place_form.name, place_form.street, place_form.number,
                       place_form.neighbor, place_form.city, place_form.state, coordinates.latitude,
                       coordinates.longitude, None)

        insert_place(place.__dict__)
        flash("Local cadastrado com sucesso!")
    except:
        flash("Erro ao adicionar local")
    return redirect(url_for('administration.places'))


@administrator.route('/admin/locais/listalocal')
@admin_route
def list_place():
    return render_template('admin/list_places.html', titulo="Editar locais", places=list_all_places(),
                           imagem='imgs/add_place.jpg')


@administrator.route('/admin/locais/listalocal/editarlocal<string:place_id>')
@admin_route
def edit_places(place_id):
    result = ''
    try:
        result = find_by_id(place_id)
    except:
        flash("Não é possível editar este local")
    return render_template('admin/edit_place.html', titulo="Editar local",
                           imagem='imgs/add_place.jpg', place=result, place_id=place_id)


@administrator.route('/admin/locais/listalocal/submitedit', methods=['POST', ])
def submit_edit():
    try:
        place_form = PlaceVO(request.form)

        if not valid_cep(place_form.cep):
            return redirect(url_for('administration.edit'))

        coordinates = get_coordinates(place_form.to_string())
        # Recebe o _id do local, para o find do local no banco pelo Object ID
        place_id = str(request.form['place_id'])
        # Recebe o ID do local
        placeid = str(request.form['placeid'])
        place = Places(placeid, place_form.cep, place_form.name, place_form.street, place_form.number,
                       place_form.neighbor, place_form.city, place_form.state, coordinates.latitude,
                       coordinates.longitude, None)
        update_place(place_id, place.__dict__)
        flash("Editado com sucesso!")
    except:
        flash("Erro ao editar")
    return redirect(url_for('administration.list_place'))


@administrator.route('/admin/locais/listalocal/removerlocal<string:place_id>')
@admin_route
def remove_place(place_id):
    try:
        delete_place(place_id)
        flash("Removido com sucesso")
    except:
        flash("Não foi possível remover local")
    return redirect(url_for('administration.list_place'))


@administrator.route('/admin/locais/listausuarios')
@admin_route
def manage_users():
    users = list_all_users()
    if not users:
        flash("Nenhum usuário encontrado")
    return render_template('admin/users.html', titulo="Administrar usuários", users=users, imagem='imgs/signinup.jpg')


@administrator.route('/admin/locais/listausuarios/removerusuario<string:id>')
@admin_route
def remove_user(user_id):
    try:
        delete_user(user_id)
    except:
        flash("Não foi possível deletar usuário")
    return redirect(url_for('administration.manage_users'))
