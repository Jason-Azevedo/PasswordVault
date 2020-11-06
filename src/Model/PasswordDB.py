import sqlite3

class PasswordDB:
    # conn: sqlite database connection
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()
        self.setup_db()

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
        
