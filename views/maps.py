from flask_googlemaps import Map
from geopy.geocoders import GoogleV3 # Api GMAPS

# Transforma um endereço(numero + rua + bairro + cidade + estado) em coordenadas
def coordenates(address):
    place = GoogleV3(timeout=30, api_key="AIzaSyBybFqISUIGfRoLJoSyDUOa_4N4pRUIF8g")
    coordenate = place.geocode(address)
    return coordenate

# Recebe os endereços do banco de dados e cria uma lista no formato aceito pela API do mapa
def map_address(places):
    adresses = []
    # Para cada endereço no banco lugares
    for i in range(0, len(places)):
        # Cria um infobox com: Nome, rua, numbero, bairro, cidade, estado e o CEP que será
        # apresentado no mapa
        infobox = (
            '<div style="font-size:18px"><b>' + 
                (places[i]['name']) + '</b>' + 
            '</div>' + 
            '<div style="font-size:14px">' +
                '<div>'+ (places[i]['street']) + ', ' + (places[i]['number']) + '</div>' +
                '<div>' + (places[i]['neighbor']) + ' - ' + (places[i]['city']) + '</div>' +
                '<div>' + (places[i]['state']) + ' - ' + (places[i]['cep']) + '</div>' +
            '</div>'
            )
        # Armazena na lista o endereço no novo formato
        adresses.append((places[i]['lat'], places[i]['lng'], infobox, places[i]['icon']))
    return adresses

# Retorna uma instancia do tipo MAP com os dados para criar o mapa
def maps(places):
    return Map(
        identifier="movingmap",
        varname="movingmap",
        # latitude padrão quando abrir o mapa
        lat=places[0]['lat'],
        # longitude padrão quando abrir o mapa
        lng=places[0]['lng'],
        # Distancia do mapa
        zoom=9,
        # Tamanho do mapa
        style="height:400px;width:100%;",
        # Pontos do mapa
        markers=map_address(places)
    )
 

