from Model.PasswordDB import PasswordDB
from Interpreter import Interpreter
from os import path
import sqlite3
import sys

# Setup
dbPath = path.join(
    path.dirname(path.realpath(__file__)), 'pwd.db')

db_conn = sqlite3.connect(dbPath)
passwordDB = PasswordDB(db_conn)

def Auth():
    # Get the correct pass from passwordDB
    correct_pass = 'pass'

    if '-p' in sys.argv:
        password = sys.argv[2]
    else:
        password = input('Password: ')

    if password == correct_pass:
        return True
    else:
        return False


if __name__ == "__main__":
    interpreter = Interpreter()

    # Login
    if Auth():
        print('Successfully logged in')
        if '-p' in sys.argv and len(sys.argv) > 3:
            cmd = ''

            for i in range(3, len(sys.argv)):
                cmd += sys.argv[i] + ' '

            interpreter.execCommand(cmd) 

        else:
            interpreter.Interpret()
    else:
        print('Password incorrect')

    # Exit the program
    passwordDB.close()