import sqlite3


class PasswordDB:
    # conn: sqlite database connection
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()
        self.setup_db()

    def get_all(self):
        query = 'SELECT * FROM Passwords'
        return self.cursor.execute(query).fetchall()

    def get(self, name):
        query = 'SELECT * FROM Passwords WHERE passFor = ?'
        return self.cursor.execute(query, [name]).fetchone()

    def new(self, name, password):
        entry_exist_query = 'SELECT * FROM Passwords WHERE passFor = ?'
        query = 'INSERT INTO Passwords (passFor, password) VALUES (?, ?)'

        if len(self.cursor.execute(entry_exist_query, [name]).fetchall()) >= 1:
            return False

        self.cursor.execute(query, [name, password])
        self.conn.commit()
        return True

    def edit(self, name, new_name, new_pass):
        query = '''UPDATE Passwords SET 
                    passFor = ?,
                    password = ?
                    WHERE passFor = ?'''

        self.cursor.execute(query, [new_name, new_pass, name])
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
            self.cursor.execute(create_user_query, ['user', 'pass'])

            print('Account setup: \nname: user\npassword: pass\n')

        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
