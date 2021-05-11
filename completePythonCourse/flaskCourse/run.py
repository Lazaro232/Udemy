from app import app
from app.controllers import default


# Apenas questão de segurança (só roda se for o MAIN rodando)
if __name__ == '__main__':
    app.run(debug=True)
