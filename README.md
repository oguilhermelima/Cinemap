# MAPA

Página que permite um usuário se cadastrar e salvar os locais mais próximos de um CEP.
## Recursos: ##
**Usuários:**
* Cadastro e login
* Editar perfil
* Pesquisa de locais próximos de um CEP
* Salvar locais pesquisados

**Administrador**
* Cadastro de novos locais
* Gestão de locais (edição e remoção)
* Gestão de usuários

## Deploy no HEROKU

**LINK HEROKU - [MAPA](http://mapacultural.herokuapp.com/).**

## Deploy

### Python ###

Download e instalação da versão mais recente do Python

**Windows** - [Python](https://www.python.org/downloads/).

**Linux** - A maioria das versões linux já vem com python3 instalado.

### PIP ###

Agora, faça a instalação do Pip para Python 3

**Linux**
```
sudo apt-get install python3-pip
```

**Não é necessário a instalação do PIP no windows**

### Clone do repositório ###

**Opção 1: Faça o download do repositório** - [Download](https://github.com/oguilherme-lima/maps/archive/master.zip)

Extraia o ZIP, e acesse **maps-master**

**Opção 2: Faça o clone pelo Git Bash**
```
git clone https://github.com/oguilherme-lima/maps.git
```
Depois digite
```
cd maps
```

### Pacotes

**Opção 1: No mesmo diretório do requiriments.txt execute:**

**Windows**
```
pip3 install -r requirements.txt
```

**Linux**
```
sudo pip3 install -r requirements.txt
```

**Opção 2: execute no terminal**

**Windows**
```
pip3 install flask pymongo==2.8.1 flask_googlemaps==0.2.6 geopy==1.13.0 pycep-correios==2.3.1 flask-login
```
**Linux**
```
sudo pip3 install flask pymongo==2.8.1 flask_googlemaps==0.2.6 geopy==1.13.0 pycep-correios==2.3.1 flask-login
```
### Exportar e rodar a aplicação

**Windows**
```
set FLASK_APP=Api.py
```
```
flask run
```
**Linux**
```
export FLASK_APP=Api.py
```
```
flask run
```

**Agora é só acessar a url http://127.0.0.1:5000/**


## Construído com
* [Python](https://python.org/) - Linguagem de programação
* [Flask](http://flask.pocoo.org/) - Microframework Web
* [Flask Login](https://flask-login.readthedocs.io/en/latest/) - Gestão de usuários
* [Geopy](http://geopy.readthedocs.io) - API que gera coordenadas a partir de um endereço
* [Flask_GoogleMaps](https://github.com/rochacbruno/Flask-GoogleMaps) - API que constrói um mapa baseado na Google Maps JavaScript API
* [PyCEPCorreios](https://pycep-correios.readthedocs.io/) - API de consulta de CEP
* [pyMongo](https://api.mongodb.com/python/current/) - Pacote que permite a conexão entre o Python e o banco de dados Mongo