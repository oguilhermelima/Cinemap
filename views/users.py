from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, name, password, email, type):
        self._id = username
        self.name = name
        self.password = password
        self.email = email
        self.type = type

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id