import sqlite3


class Database:
    def __init__(self) -> None:
        connection = sqlite3.connect('bancoDados.db')
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE if not exists clients(id INTEGER PRIMARY KEY, pessoa TEXT,
        nome TEXT, cpf TEXT, email TEXT, contato TEXT)"""
                       )
        connection.commit()
        connection.close()

    def add_client(self, pessoa, nome, cpf, email, contato):
        connection = sqlite3.connect('bancoDados.db')
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO clients (pessoa, nome, cpf, email, contato)
        VALUES (?, ?, ?, ?, ?)""", (pessoa, nome, cpf, email, contato))
        connection.commit()
        connection.close()

    def update_client(self, id, pessoa, nome, cpf, email, contato):
        connection = sqlite3.connect('bancoDados.db')
        cursor = connection.cursor()
        cursor.execute("""
        UPDATE clients SET pessoa=?, nome=?, cpf=?, email=?, contato=?
        WHERE id=?""", (pessoa, nome, cpf, email, contato, id)
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
        connection.close()
        return records
