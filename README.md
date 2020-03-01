# CINEMAPS

Página que permite um usuário buscar e salvar os cinemas mais próximos de um CEP na região de São Paulo.
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

**LINK HEROKU - [CINEMAPS](http://cinemaps.herokuapp.com).**

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

Agora faça a instalação dos pacotes necessários para rodar a aplicação.

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
pip3 install gunicorn==19.8.1 flask==0.12.2 pymongo==2.8.1 flask_googlemaps==0.2.6 geopy==1.13.0 pycep-correios==2.3.1 flask-login flask_compress
```
**Linux**
```
sudo pip3 install gunicorn==19.8.1 flask==0.12.2 pymongo==2.8.1 flask_googlemaps==0.2.6 geopy==1.13.0 pycep-correios==2.3.1 flask-login flask_compress
```
### Exportar e rodar a aplicação

Por fim, para inicializar a aplicação, digite os comandos abaixo:

**Windows**
```
set FLASK_APP=app.py
```
```
flask run
```
**Linux**
```
export FLASK_APP=app.py
```
```
flask run
```

**Agora é só acessar a url http://127.0.0.1:5000/**


## Construído com
* [Python](https://python.org/) - Linguagem de programação
* [Flask](http://flask.pocoo.org/) - Microframework Web
* [Flask Compress](https://github.com/libwilliam/flask-compress) - Compressão das respostas da aplicação com GZIP
* [Flask GoogleMaps](https://github.com/rochacbruno/Flask-GoogleMaps) - API que constrói um mapa baseado na Google Maps JavaScript API
* [Flask Login](https://flask-login.readthedocs.io/en/latest/) - API para gestão de usuários
* [Geopy](http://geopy.readthedocs.io) - API que gera coordenadas a partir de um endereço
* [PyCEPCorreios](https://pycep-correios.readthedocs.io/) - API de consulta de CEP
* [pyMongo](https://api.mongodb.com/python/current/) - Pacote que permite a conexão entre o Python e o banco de dados Mongo
