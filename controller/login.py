from werkzeug.security import generate_password_hash as p_hash, check_password_hash as c_hash
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user
from util.decorators import is_not_logged_in
from util.validations import valid_user
from file.modelsVO import SubscriptionVO
from file.models import User
from database import db_users

log_in = Blueprint('signin', __name__)


# Rota de cadastro
@log_in.route('/registrar')
@is_not_logged_in
def register():
    return render_template('signup.html', titulo='Sign up', imagem='imgs/signinup.jpg')


# Rota para autenticar o cadastro
@log_in.route('/novousuario', methods=['POST'])
@is_not_logged_in
def new_user():
    subscription = SubscriptionVO(request.form)
    # Verifica se o usuario e email já constam no banco de dados
    if not valid_user(subscription.username, subscription.email, subscription.password, subscription.confirm_password):
        # Se existir, retorna para a página de registro
        return render_template('signup.html', titulo='Sign up', imagem='imgs/signinup.jpg',
                               username=subscription.username, email=subscription.email, name=subscription.name)
    # Faz o hash da senha
    password = p_hash(request.form['psw'], method='sha256')
    # Armazena no MongoDB
    db_users.add_user(User(subscription.username, subscription.name, password, subscription.email, "user").__dict__)
    # Apresenta mensagem para o usuário
    flash("Usuário cadastrado com sucesso!")
    # Redireciona para a tela de login
    return redirect(url_for('signin.login'))


# Rota de Login
@log_in.route('/entrar')
@is_not_logged_in
def login():
    return render_template('login.html', titulo='Sign in', imagem='imgs/signinup.jpg')


@log_in.route('/autenticar', methods=['POST'])
def authenticate():
    user_database = db_users.find_user(request.form['usuario'])
    if user_database:
        if c_hash(user_database['password'], request.form['senha']):
            login_user(User(user_database['_id'], user_database['name'], user_database['password'],
                            user_database['email'], 'user'))
            return redirect(url_for('index.home'))
        else:
            flash("Senha inválida")
    else:
        flash("Username inválido")
    # Se a senha e usuário não estiverem corretos, redireciona para a página de login        
    return redirect(url_for('signin.login'))


# Rota de logout
@log_in.route('/sair')
def logout():
    logout_user()
    return redirect(url_for('index.home'))
