from flask import Blueprint, render_template, request, flash
from pycep_correios import consultar_cep as check_cpf
from database.db_places import list_places_by_user, list_all_places
from service.maps_service import create_map_pin, get_coordinates
from file.models import Places

index = Blueprint('index', __name__)


@index.route('/')
def home():
    qtt = 20
    accordion = False
    cep = request.args.get('cep')
    result = logged_in_user_place(cep)
    if result:
        accordion = True
        qtt = int(request.args.get('qtt'))
        places = list_places_by_user(result, qtt)
    else:
        places = list_all_places()

    new_map = create_map_pin(places)
    return render_template('index.html', titulo='CineMap',
                           places=places, accordion=accordion, movingmap=new_map, cep=cep, qtt=qtt, user=result)


def logged_in_user_place(cep):
    try:
        full_address = check_cpf(cep)
        address = get_coordinates(full_address['end'] + full_address['bairro'] + full_address['cidade'] + full_address['uf'])

        return Places(0, cep, 'Meu local', full_address['end'], "n/h", full_address['bairro'],
                      full_address['cidade'], full_address['uf'], address.latitude, address.longitude,
                      "../static/imgs/marker.png").__dict__
    except:
        if cep:
            flash("CEP incorreto. Não foi possível encontra-lo")
        return ''

