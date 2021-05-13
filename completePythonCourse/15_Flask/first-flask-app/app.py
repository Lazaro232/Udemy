from flask import Flask

# O objeto Flask deve ÚNICO. Para garantir isso, usa-se o nome
# da aplicação que está rodando (__main__, por exemplo )
app = Flask(__name__)


@app.route('/')  # Página inicial
def home():
    return 'Hello, world!'


# Garante que quem está rodando é o MAIN
if __name__ == '__main__':
    app.run(debug=True)
