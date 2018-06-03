from flask import Blueprint, render_template, session, redirect, url_for, request, flash
import pycep_correios # Api correios que recebe o CEP e retorna o Endereço
from .db_places import find_places
from .maps import maps, coordenates
from .places import Places

ind = Blueprint('index', __name__)

@ind.route('/')
def index():
    new_map = ''
    table = False
    cep = ''
    # Verifica se existe um CEP digitado, se sim, busca os locais próximos no banco de dados
    # Se não, apresenta todos os locais
    user = temp_user()
    # Se existir um CEP digitado, também cria uma tabela para apresentar os locais
    if user:
        table = True
        cep = str(user['cep'])
    # Busca e retorna os locais
    places = find_places(user)
    # Verifica a quantidade de locais
    num_places = len(places)
    # Se existir locais, carrega o mapa
    if num_places:
        # Recebe as coordenadas e nomes dos pontos que serão colocados no mapa
        new_map = maps(places)
    # Retorna a lista com os locais e cria o mapa
    return render_template('index.html', titulo='Mapa Cultural', subtitulo='São Paulo',
        places=places, table=table, movingmap=new_map, num_places=num_places, cep=cep)

# Retorna o endereço do CEP inserido pelo usuário
def temp_user():
    place = ''
    # Recebe o valor da variavel cep da uri
    cep_uri = request. args.get('cep')
    try:
    	# Tenta consultar o CEP
    	# Retorna um endereço completo (Rua, bairro, cidade, estado e o próprio CEP)
    	cep = pycep_correios.consultar_cep(cep_uri)
    except:
        if cep_uri:
            flash("CEP incorreto. Não foi possível encontra-lo")
        return place
    # Recebe o conteudo do CEP    
    name = 'Meu local'
    street = cep['end']
    neighbor = cep['bairro'] 
    city = cep['cidade']
    state = cep['uf']
    # Chama a função coordenadas, passando um endereço quase completo e recebe as coordenadas do ponto
    address = coordenates(street + neighbor + city + state)
    # Armazena um dicionario dos atributos da instancia de Locais
    place = (Places(0,cep_uri, name, street, "n/h", neighbor, city, state,
               address.latitude, address.longitude, "../static/imgs/marker.png").__dict__)
    return place