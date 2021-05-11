from app import manager
from app.controllers import default


# Apenas questão de segurança (só roda se for o MAIN rodando)
if __name__ == '__main__':
    manager.run()
