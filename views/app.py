from flask import Flask, render_template
from whitenoise import WhiteNoise
from flask_login import LoginManager
from flask_googlemaps import GoogleMaps
from .db_users import find_user
from .users import User
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static') 
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'WYZ')

# GZIP
app.wsgi_app = WhiteNoise(app.wsgi_app)
my_static_folders = (
	'../static/fonts/',
    '../static/fonts/montserrat/',
    '../static/fonts/poppins/',
    '../static/imgs/',
    '../static/js/',
    '../static/styles/',
    '../static/styles/fonts/',
    '../static/templates/',
    '../static/templates/admin',
    '../static/templates/template',
)
for static in my_static_folders:
    app.wsgi_app.add_files(static)

# Não retorna 404 quando o usuário insere slash(/) no final da URI
app.url_map.strict_slashes = False

# Configura o Flask Login
login_manager = LoginManager()
login_manager.init_app(app)

# Pagina padrão para o login required
login_manager.login_view = 'signin.login'

# Verifica e retorna o usuário logado
@login_manager.user_loader
def load_user(username):
    user = find_user(username)
    if not user:
        return None
    return User(user['_id'], user['name'], user['password'], user['email'], user['type'])

# Configura a api do Gmaps
GoogleMaps(app, key="AIzaSyBybFqISUIGfRoLJoSyDUOa_4N4pRUIF8g")

# Pagina Not Found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html'), 404
