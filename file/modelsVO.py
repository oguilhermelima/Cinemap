class PlaceVO:
    def __init__(self, form):
        self.cep = form['cep']
        self.name = form['nome']
        self.street = form['rua']
        self.number = form['numero']
        self.neighbor = form['bairro']
        self.city = form['cidade']
        self.state = form['estado']

    def to_string(self):
        return self.number + self.street + self.neighbor + self.city + self.state


class SubscriptionVO:
    def __init__(self, form):
        self.name = form['nome']
        self.username = form['usuario']
        self.password = form['psw']
        self.confirm_password = form['password']
        self.email = form['email']