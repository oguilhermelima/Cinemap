# MAPA

Página que busca, armazena endereços e os apresentam no Google Maps. Também é possível buscar os locais salvos mais próximos de um CEP.

## Deploy no HEROKU

**Link**: [HEROKU](mapacultural.herokuapp.com/).

## Deploy

Download e instalação da versão mais recente do Python

**Windows** - [Python](https://www.python.org/downloads/).

**Linux** - A maioria das versões linux já vem com python3 instalado.

Agora, faça a instalação do Pip para Python 3

**Linux**
```
sudo apt-get install python3-pip
```

**Não é necessário a instalação do PIP no windows**

### Pacotes

No diretório do **requiriments.txt** execute:

**Windows**
```
pip3 install -r requirements.txt
```

**Linux**
```
sudo pip3 install -r requirements.txt
```

**Ou execute no terminal**

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
* [Geopy](http://geopy.readthedocs.io) - API que gera coordenadas a partir de um endereço
* [Flask_GoogleMaps](https://github.com/rochacbruno/Flask-GoogleMaps) - API que constrói um mapa baseado na Google Maps JavaScript API
* [PyCEPCorreios](https://pycep-correios.readthedocs.io/) - API de consulta de CEP
* [pyMongo](https://api.mongodb.com/python/current/) - Pacote que permite a conexão entre o Python e o banco de dados Mongo