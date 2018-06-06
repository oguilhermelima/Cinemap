from flask import Blueprint, request, redirect, flash, render_template, url_for
from .db_places import insert_places, find_by_id, find_places, edit_place, remove_place
from .validations import is_adm, check_cep
from .db_users import return_users, delete_user
from .maps import coordenates
from .places import Places

administrator = Blueprint('administration', __name__)

# Menu com o painel para controle de locais e usuários
@administrator.route('/admin')
def dashboard():
    # Verifica se o usuário é adm, se não for retorna 404
    if is_adm():
        return render_template('admin/dashboard.html', titulo="Dashboard", imagem='imgs/administration.jpg')
    else:
        return render_template('notfound.html')    

# Menu com o painel para controle de locais
@administrator.route('/admin/locais')
def places():
    # Verifica se o usuário é adm, se não for retorna 404
    if is_adm():
        return render_template('admin/places.html', titulo="Locais", imagem='imgs/newplace.jpg')
    else:
        return render_template('notfound.html')

# Formulário para adicionar um novo local
@administrator.route('/admin/locais/novolocal')
def new_place():
    # Verifica se o usuário é adm, se não for retorna 404
    if is_adm():
        return render_template('admin/new_place.html', titulo='Novo local', imagem='imgs/newplace.jpg')
    else:
        return render_template('notfound.html')

# Submit do formulario
@administrator.route('/criar', methods=['POST',])
def create_place():
    try:
        # Recebe os valores dos campos do form
        cep = request. form['cep']
        name = request. form['nome']
        street = request. form['rua']
        number = request. form['numero']
        neighbor = request. form['bairro']
        city = request. form['cidade']
        state = request. form['estado']
        # ID do local   
        id_place = (name.replace(" ", "") + str(cep) + str(number))
        # Cria um endereço unico com os dados do form para busca das coordenadas
        model = number + street + neighbor + city + state
        # Gera as coordenadas 
        address = coordenates(model)
        # Verifica se o CEP do submit é real, ou se foi alterado depois do retorno de pesquisa
        if not check_cep(cep):
            return redirect(url_for('administration.new_place'))
        # Cria uma instancia do tipo Place, que armazena um indereço completo + icone  
        place = Places(id_place, cep, name, street, number, neighbor, city, state,
                       address.latitude, address.longitude, None)
        # insere no banco a instancia convertida para dicionario
        insert_places(place.__dict__)
        # Rota dinâmica pra função index
        flash("Local cadastrado com sucesso!")
    except:
        flash("Erro ao adicionar local")
    return redirect(url_for('administration.places'))

# Lista todos os locais cadastrado
@administrator.route('/admin/locais/listalocal')
def listplace():
    # Verifica se o usuário é adm, se não for retorna 404
    if is_adm():
        # Busca os locais no banco de dados
        places = find_places(0,0)
        return render_template('admin/list_places.html', titulo="Editar locais", places=places, 
            imagem='imgs/newplace.jpg')
    else:
        return render_template('notfound.html')

# Formulario que recebe os dados do banco e permite editar as informações
@administrator.route('/admin/locais/listalocal/editarlocal<string:id>')
def edit(id):
    # Verifica se o usuário é adm, se não for retorna 404
    if is_adm():
        try:
            # Busca o local pelo ID
            result = find_by_id(id)
        except:
            flash("Não é possível editar este local")
        return render_template('admin/edit_place.html', titulo="Editar local",  
            imagem='imgs/newplace.jpg', place=result, place_id=id)
    else:
        return render_template('notfound.html')

# Submit da rota edit
@administrator.route('/admin/locais/listalocal/submitedit', methods=['POST',])
def submit_edit():
    try:
        # Recebe os valores dos campos do form
        cep = request. form['cep']
        name = request. form['nome']
        street = request. form['rua']
        number = request. form['numero']
        neighbor = request. form['bairro']
        city = request. form['cidade']
        state = request. form['estado']
        # Cria um endereço unico com os dados do form para busca das coordenadas
        model = number + street + neighbor + city + state
        # Verifica se o CEP do submit é real, ou se foi alterado depois do retorno de pesquisa
        if not check_cep(cep):
            return redirect(url_for('administration.edit'))
        # Gera as coordenadas 
        address = coordenates(model)
        # Recebe o _id do local, para o find do local no banco pelo Object ID
        place_id = str(request. form['place_id'])
        # Recebe o ID do local
        placeid = str(request. form['placeid'])
        # Cria uma instancia do tipo Place, que armazena um indereço completo + icone  
        place = Places(placeid, cep, name, street, number, neighbor, city, state,
                       address.latitude, address.longitude, None)
        # insere no banco a instancia convertida para dicionario
        edit_place(place_id, place.__dict__)
        flash("Editado com sucesso!")
    except:
        flash("Erro ao editar")
    return redirect(url_for('administration.listplace'))

# Botão que remove o local da lista de locais
@administrator.route('/admin/locais/listalocal/removerlocal<string:id>')
def remove(id):
    try:
        # Remove o usuário pelo ID
        remove_place(id)
        flash("Removido com sucesso")
    except:
        flash("Não foi possível remover local")
    return redirect(url_for('administration.listplace'))

# Rota que permite gerenciar os usuários
@administrator.route('/admin/locais/listausuarios')
def manage_users():
    # Verifica se o usuário é adm, se não for retorna 404
    if is_adm():
        try:
            # Busca todos os usuários
            users = return_users()
        except:
            flash("Nenhum usuário encontrado")
        return render_template('admin/users.html', titulo="Administrar usuários", users=users, 
            imagem='imgs/signinup.jpg')
    else:
        return render_template('notfound.html')

# Botão que remove o usuário selecionado
@administrator.route('/admin/locais/listausuarios/removerusuario<string:id>')
def remove_user(id):
    # Verifica se o usuário é adm, se não for retorna 404
    if is_adm():
        try:
            # Deleta usuário do banco de dados
            delete_user(id)
        except:
            flash("Não foi possível deletar usuário")
        return redirect(url_for('administration.manage_users'))
    else:
        return render_template('notfound.html')