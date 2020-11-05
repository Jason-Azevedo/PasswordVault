from Model.PasswordDB import PasswordDB
from Interpreter import Interpreter
import sqlite3
from os import path

# Setup
dbPath = path.join(
    path.dirname(path.realpath(__file__)), 'pwd.db')

db_conn = sqlite3.connect(dbPath)
passwordDB = PasswordDB(db_conn)

def Auth():
    pass


if __name__ == "__main__":
    # Login
    Auth()

    # Execute action from args or enter interpreter mode

    # Exit the program
    passwordDB.close()