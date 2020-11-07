import os
from Model.PasswordDB import PasswordDB


class Interpreter:
    def __init__(self, passDB: PasswordDB):
        self.db = passDB

    def execCommand(self, cmd):
        if 'exit' in cmd or 'quit' in cmd:
            return 0
        elif 'help' in cmd:
            self.print_commands()
        elif 'cls' in cmd or 'clear' in cmd:
            self.clear_screen()
        elif 'show-all' in cmd or '--show-all' in cmd:
            self.show_all()

        else:
            print('\'' + cmd + '\'', 'Command not found')

    def print_commands(self):
        print('List of available commands:')
        print('---------------------------')
        self.print_table_value('exit/quit', 'Closes the program')
        self.print_table_value('help', 'List all available commands')
        self.print_table_value('cls/clear', 'Clears the screen')
        self.print_table_value('show-all', 'Shows all passwords')
        self.print_table_value('show <name>', 'Shows the password for that entry')
        self.print_table_value('new <name> <pass>', 'Creates a new password entry')
        self.print_table_value('show <name>', 'Shows the password for that entry')
        self.print_table_value('edit <name>', 'Edit an existing password entry')
        self.print_table_value('del <name>', 'Removes a password entry')

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def show_all(self):
        passEntries = self.db.get_all()
        
        self.print_table_value('Entry', 'Password')
        print('----------------------------------')

        for entry in passEntries:
            self.print_table_value(entry[0], entry[1])

    def show(self, name):
        pass

    def new(self, name, password):
        pass

    def edit(self, name):
        pass

    def delete(self, name):
        pass

    def print_table_value(self, x, y):
        print('{:<25} {:<20}'.format(x, y))

    def Interpret(self):
        print('Enter command below, help to list all commands, exit/quit to close program')
        while True:
            try:
                cmd = input('> ')
            except EOFError:
                print('EOF Error occured')
            except KeyboardInterrupt:
                break

            if self.execCommand(cmd) == 0:
                break
