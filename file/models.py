from flask_login import UserMixin


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

        self.lat = latitude
        self.lng = longitude
        self.coordinates = [latitude, longitude]
        self.icon = icon


class User(UserMixin):
    def __init__(self, username=None, name=None, password=None, email=None, category=None):
        self._id = username
        self.name = name
        self.password = password
        self.email = email
        self.category = category

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id