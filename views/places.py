# Cria um objeto do tipo Local
class Places:
    def __init__(self, id, cep, name, street, number, neighbor, city, state, latitude, longitude, icon):
        self.id = id
        self.cep = cep
        self.name = name
        self.street = street
        self.number = number
        self.neighbor = neighbor
        self.city = city
        self.state = state

        # Utilizado no Mapa
        self.lat = latitude
        self.lng = longitude
        self.coordinates = [latitude, longitude]
        self.icon = icon
 
