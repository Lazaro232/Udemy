from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_login import LoginManager


# Configurando o Objeto Flask
app = Flask(__name__)
# Configurando o banco de dados usando SQLAlchemy
# Passa as configurações do Flask/Banco de dados ...
# ... usando um arquivo dedicado (config.py)
app.config.from_object('config')
db = SQLAlchemy(app)
# Configurando as migrações
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager(app)  # Login Manager


# Para iniciar a pasta MIGRARIONS: python3 run.py db init
# Migrando as mudanças:   python3 run.py db migrate (Ainda não cria as tabelas)
# Aplicando as Migrações acima:    python3 run.py db upgrade
# Rodando server:                  python3 run.py runserver
