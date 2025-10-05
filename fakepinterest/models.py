# Definição (Estrutura) do banco de dados

from fakepinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin


# Função padrão, obrigatória, que carrega o usuario
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario)) # Retorna a classe reponsável pelos logins


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True) # relaciona as fotos de um usuario do objeto Foto no banco de dados


class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False) #chave extrangeira do usuario

