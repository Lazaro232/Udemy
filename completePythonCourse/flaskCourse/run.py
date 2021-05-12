from app import manager
from app.controllers import default
from app.models import tables


# Apenas questão de segurança (só roda se for o MAIN rodando)
if __name__ == '__main__':
    manager.run()
