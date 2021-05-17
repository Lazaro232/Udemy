import sqlite3

'''
Arquivo que contém funções que interagem com o banco de dados
'''


def create_investment_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS investments(id INTEGER PRIMARY KEY, ativo TEXT,
        numero_cotas INTEGER, valor_cota FLOAT(24), data TIMESTAMP)'''
    )
    connection.commit()
    connection.close()


def add_investment(ativo, numero_cotas, valor_cota, data):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(
        '''INSERT INTO investments (ativo, numero_cotas, valor_cota, data)
        VALUES (?, ?, ?, ?)''',
        (ativo, numero_cotas, valor_cota, data))
    connection.commit()
    connection.close()


def get_all_investments():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM investments')

    investments = [{'id': row[0],
                    'ativo': row[1],
                    'numero_cotas': row[2],
                    'valor_cota': row[3],
                    'data': row[4]} for row in cursor.fetchall()]
    connection.close()
    return investments


def delete_investment(id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM investments WHERE id = ?', (id,))
    connection.commit()
    connection.close()
