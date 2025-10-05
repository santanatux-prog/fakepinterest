from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto

# Cria a instancia do banco de dados (vazio, sem as tabelas)
with app.app_context():
    database.create_all()


# Cria uma chave de segurança aleatoria
import secrets
print(secrets.token_hex(16))