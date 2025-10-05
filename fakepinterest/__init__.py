from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


# Criação da aplicação
app = Flask(__name__)

# Variavel que indica o local do banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "25abf2f162e92454b5e55d4a683ca2d0" #Chave que proteje a sessão do usuário
app.config["UPLOAD_FOLDER"] = "static/fotos_posts" # Diretorio das postagens dos usuários

database = SQLAlchemy(app) # Cria o banco de dados dentro da aplicação
bcrypt = Bcrypt(app) # Faz a criptografia de senhas dos usuários
login_manager = LoginManager(app) # Faz o gerenciamento dos Logins
login_manager.login_view = "homepage" # Direciona para pagina que faz login, caso nenhum usuário tiver logado

from fakepinterest import routes
