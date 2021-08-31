import sqlite3


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


def update_investment(id, ativo, numero_cotas, valor_cota, data):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(
        '''UPDATE investments SET ativo=?, numero_cotas=?, valor_cota=?, data=? WHERE id=?''',
        (ativo, numero_cotas, valor_cota, data, id))
    connection.commit()
    connection.close()


def delete_investment(id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM investments WHERE id = ?', (id,))
    connection.commit()
    connection.close()
