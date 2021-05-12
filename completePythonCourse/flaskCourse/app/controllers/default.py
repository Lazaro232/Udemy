from flask import render_template, flash, redirect, url_for
from flask_login import login_manager
from flask_login.utils import login_user, logout_user

from app.models.tables import User

from app import app, db

# from app.models.tables import User
from app.models.forms import LoginForm


@app.route('/index/<user>')  # Página Inicial
@app.route('/', defaults={"user": None})
def index(user):
    return render_template('index.html',
                           user=user)  # Recebe HTML e renderiza


@app.route('/login', methods=['GET', 'POST'])  # Página de Login
def login():
    form = LoginForm()
    if form.validate_on_submit():  # Verificando se o From foi validado
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for('index'))
        else:
            flash("Invalid Login.")

    return render_template('login.html', form=form)


@app.route('/logout')  # Página de Logout
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for('index'))


'''
COMO FAZER CRUD (INSERT, SELECT, UPDATE, DELETE) -- BANCO DE DADOS

@app.route("/insert/<info>")  # Inserindo Usuário (INSERT)
@app.route("/insert", defaults={'info': None})
def insert(info):
    i = User('Lazarone123', '3264', 'Lazaro Neto', 'jose1@gmail.com')
    db.session.add(i)  # Inicia a sessão com o Banco de Dados
    db.session.commit()  # Salva as informações da sessão
    return 'OK'


@app.route("/select/<info>")  # Pesquisando Usuário (SELECT)
@app.route("/select", defaults={'info': None})
def select(info):
    r = User.query.filter_by(password="3264").all()
    print(r)
    return 'OK'


@app.route("/update/<info>")  # Atualizando dado do usuário (UPDATE)
@app.route("/update", defaults={'info': None})
def update(info):
    r = User.query.filter_by(username="Lazarone123").first()
    # Usando o 'first()', pode-se acessar os parâmetros do registro 'r'
    print(r.username, r.name)

    # Update --> Alterando o NOME do usuário
    r.name = "Jose Lazaro Neto"
    db.session.add(r)
    db.session.commit()
    print(r.username, r.name)
    return 'OK'


@app.route("/delete/<info>")  # Deltando um usuário (DELETE)
@app.route("/delete", defaults={'info': None})
def delete(info):
    r = User.query.filter_by(username="Lazarone123").first()

    # Deletando
    db.session.delete(r)
    db.session.commit()
    return 'OK'
'''

'''
COMO PASSAR PARÂMETROS NOS ENDPOINTS

@app.route('/test', defaults={'name': None})  # Passando String para o ENDPOINT
@app.route('/test/<name>')
def test(name):
    if name:
        return f'Olá, {name}'
    else:
        return 'Olá Usuário'

# methods --> Indica os métodos http aceitos
# Passando Inteiro para o ENDPOINT


@app.route('/test/<int:id>', methods=['GET'])
def testId(id):
    return f'Olá ID: {id}'
'''
