from flask import render_template
from app import app, db

# from app.models.tables import User
from app.models.forms import LoginForm


@app.route('/index/<user>')
@app.route('/', defaults={"user": None})
def index(user):
    return render_template('index.html',
                           user=user)  # Recebe HTML e renderiza


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # Verificando se o From foi validado
        print(form.username.data)
        print(form.password.data)

    return render_template('login.html', form=form)


'''
@app.route("/test/<info>")
@app.route("/test", defaults={'info': None})
def test(info):
    i = User('Lazaro232', '1234', 'Jose Lazaro', 'email@gmail.com')
    db.session.add(i)  # Inicia a sessão com o Banco de Dados
    db.session.commit()  # Salva as informações da sessão
'''

'''
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
