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
        elif 'show' in cmd or '--show' in cmd:
            self.show(cmd.split(' ')[1])
        elif 'new' in cmd or '--new' in cmd:
            try:
                name = cmd.split(' ')[1]
                password = cmd.split(' ')[2]
            except IndexError:
                print('Please enter values, use help command for more info')
                return

            if name == '' or password == '':
                print('Please enter proper values')
                return

            if self.new(name, password):
                print('New entry created')
            else:
                print('Entry already exists')

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
        print('\n')

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
        
        print('')

    def show(self, name):
        entry = self.db.get(name)
        name = entry[0]
        password = entry[1]

        self.print_table_value('Entry', 'Password')
        print('----------------------------------')
        self.print_table_value(name, password)
        print('')

    def new(self, name, password):
        self.db.new(name, password)

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
