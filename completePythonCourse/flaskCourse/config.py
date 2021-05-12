import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

# Com DEBUG = True, não precisa encerrar o servidor para novas alterações...
# ... basta salvar que o servidor roda de novo
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True  # Suprime algumas Warns do banco de dados

SECRET_KEY = 'um-nome-bem-seguro'
