from flask import render_template
from app import app


@app.route('/index/<user>')
@app.route('/', defaults={"user": None})
def index(user):
    return render_template('index.html',
                           user=user)  # Recebe HTML e renderiza


@app.route('/login')
def login():
    return render_template('base.html')


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
