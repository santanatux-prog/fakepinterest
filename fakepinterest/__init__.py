from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

# Criação da aplicação
app = Flask(__name__)

app.config["SECRET_KEY"] = "25abf2f162e92454b5e55d4a683ca2d0" #Chave que proteje a sessão do usuário

# VARIAVEL DE AMBIENTE: indica se o banco esta local ou remoto
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"

app.config["UPLOAD_FOLDER"] = "static/fotos_posts" # Diretorio das postagens dos usuários
database = SQLAlchemy(app) # Cria o banco de dados dentro da aplicação
bcrypt = Bcrypt(app) # Faz a criptografia de senhas dos usuários
login_manager = LoginManager(app) # Faz o gerenciamento dos Logins
login_manager.login_view = "homepage" # Direciona para pagina que faz login, caso nenhum usuário tiver logado

from fakepinterest import routes
