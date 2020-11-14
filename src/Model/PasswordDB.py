import sqlite3
import codecs


class PasswordDB:
    # conn: sqlite database connection
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()
        self.setup_db()

    def get_all(self):
        query = 'SELECT * FROM Passwords'
        encrypted_entries = self.cursor.execute(query).fetchall()
        entries = []

        for entry in encrypted_entries:
            entries.append([entry[0], codecs.decode(entry[1], 'rot-13')])

        return entries

    def get(self, name):
        query = 'SELECT * FROM Passwords WHERE passFor = ?'
        entry = self.cursor.execute(query, [name]).fetchone()

        return [entry[0], codecs.decode(entry[1], 'rot-13')]

    def new(self, name, password):
        entry_exist_query = 'SELECT * FROM Passwords WHERE passFor = ?'
        query = 'INSERT INTO Passwords (passFor, password) VALUES (?, ?)'
        encrypted_pass = codecs.encode(password, 'rot-13')

        if len(self.cursor.execute(entry_exist_query, [name]).fetchall()) >= 1:
            return False

        self.cursor.execute(query, [name, encrypted_pass])
        self.conn.commit()
        return True

    def edit(self, name, new_name, new_pass):
        query = '''UPDATE Passwords SET 
                    passFor = ?,
                    password = ?
                    WHERE passFor = ?'''
        encrypted_pass = codecs.encode(new_pass, 'rot-13')

        self.cursor.execute(query, [new_name, encrypted_pass, name])
        self.conn.commit()

    def delete(self, name):
        query = 'DELETE FROM Passwords WHERE passFor = ?'

        self.cursor.execute(query, [name])
        self.conn.commit()

    def setup_db(self):
        create_table_query = '''CREATE TABLE IF NOT EXISTS Passwords (
                    passFor text, 
                    password text)'''

        user_exists_query = 'SELECT * FROM Passwords WHERE passFor = \'user\''

        create_user_query = '''INSERT INTO Passwords (passFor, password)
                                 VALUES (?, ?)'''

        self.cursor.execute(create_table_query)

        if self.cursor.execute(user_exists_query).fetchone() == None:
            self.cursor.execute(create_user_query, [
                                'user', codecs.encode('pass', 'rot-13')])

            print('Account setup: \nname: user\npassword: pass\n')

        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
