import sqlite3


class Database:
    def __init__(self) -> None:
        connection = sqlite3.connect('bancoDados.db')
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE if not exists clients(id INTEGER PRIMARY KEY, nome TEXT,
        cpf TEXT, email TEXT, contato TEXT, pessoa TEXT, rg TEXT, estado TEXT,
        endereco TEXT, cidade TEXT, bairro TEXT, cep TEXT)"""
                       )
        connection.commit()
        connection.close()

    def add_client(self, nome, cpf, email, contato, pessoa,
                   rg, estado, endereco, cidade, bairro, cep):
        connection = sqlite3.connect('bancoDados.db')
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO clients (nome, cpf, email, contato, pessoa,
        rg, estado, endereco, cidade, bairro, cep)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (nome, cpf, email, contato, pessoa,
                        rg, estado, endereco, cidade, bairro, cep)
                       )
        connection.commit()
        connection.close()

    def update_client(self, id, nome, cpf, email, contato, pessoa,
                      rg, estado, endereco, cidade, bairro, cep):
        connection = sqlite3.connect('bancoDados.db')
        cursor = connection.cursor()
        cursor.execute("""
        UPDATE clients SET nome=?, cpf=?, email=?, contato=?, pessoa=?,
        rg=?, estado=?, endereco=?, cidade=?, bairro=?, cep=?
        WHERE id=?""", (nome, cpf, email, contato, pessoa,
                        rg, estado, endereco, cidade, bairro, cep, id)
                       )
        connection.commit()
        connection.close()

    def delete_client(self, id):
        connection = sqlite3.connect('bancoDados.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM clients WHERE id=?", (id,))
        connection.commit()
        connection.close()

    def query(self):
        connection = sqlite3.connect('bancoDados.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clients")
        records = cursor.fetchall()
        return records

    def query_name(self):
        connection = sqlite3.connect('bancoDados.db')
        cursor = connection.cursor()
        cursor.execute("SELECT nome FROM clients")
        names = cursor.fetchall()
        return names


if __name__ == '__main__':
    d = Database()
    lista = d.query()
    print(lista)
