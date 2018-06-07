from flask import Blueprint, render_template, request, flash
# Api correios que recebe o CEP e retorna o Endereço
from pycep_correios import consultar_cep 
from .db_places import find_places
from .maps import maps, coordenates
from .places import Places

ind = Blueprint('index', __name__)

@ind.route('/')
def index():
    # Receberá a quantidade de locais a ser pesquisado
    qtt = 0
    # Cria uma váriavel do mapa, se não existir locais, o mapa carrega sem pontos
    new_map = ''
    # Define o index sem tabela, a tabela será verdadeira quando existir um CEP digitado
    table = False
    # Receberá o CEP da URI
    cep = ''
    # Verifica se existe um CEP digitado, se sim, busca os locais próximos no banco de dados
    # Se não, apresenta todos os locais
    result = temp_user()
    # Se existir um CEP digitado 
    if result:
        # Cria uma tabela para apresentar os locais
        table = True
        # Recebe o CEP da url, utilizado para refresh
        cep = str(result['cep'])
        # Recebe a quantidade de locais a ser pesquisado
        qtt = int(request. args.get('qtt'))
    # Busca e retorna os locais
    places = find_places(result, qtt)
    # Se existir locais, carrega o mapa
    if len(places):
        # Recebe as coordenadas e nomes dos pontos que serão colocados no mapa
        new_map = maps(places)
    # Retorna a lista com os locais e cria o mapa
    return render_template('index.html', titulo='CineMap',
        places=places, table=table, movingmap=new_map, cep=cep, qtt=qtt, user=result)

# Retorna o endereço do CEP inserido pelo usuário
def temp_user():
    # Se não existir CEP, retorna uma string vazia
    place = ''
    # Recebe o valor da variavel cep da uri
    cep_uri = request. args.get('cep')
    try:
    	# Tenta consultar o CEP
    	# Retorna um endereço completo (Rua, bairro, cidade, estado e o próprio CEP)
    	cep = consultar_cep(cep_uri)
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