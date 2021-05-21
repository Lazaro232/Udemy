import sqlite3


def create_users_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name VARCHAR(50),
        password VARCHAR(50), email VARCHAR(50) UNIQUE, logo TEXT)'''
    )
    connection.commit()
    connection.close()


def add_user(name, password, email, logo):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(
        '''INSERT INTO users (name, password, email, logo)
        VALUES (?, ?, ?, ?)''',
        (name, password, email, logo))
    connection.commit()
    connection.close()


def get_all_users():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')

    users = [{'id': row[0],
              'name': row[1],
              'password': row[2],
              'email': row[3],
              'logo': row[4]} for row in cursor.fetchall()]
    connection.close()
    return users


def update_user(id, name, password, email, logo):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(
        '''UPDATE users SET name=?, password=?, email=?, logo=? WHERE id=?''',
        (name, password, email, logo, id))
    connection.commit()
    connection.close()


def delete_user(id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (id,))
    connection.commit()
    connection.close()
