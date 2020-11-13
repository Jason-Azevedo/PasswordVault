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
                print('Unable to create entry...\n')
        elif 'edit' in cmd or '--edit' in cmd:
            self.edit(cmd.split(' ')[1])
        elif 'delete' in cmd or '--delete' in cmd:
            self.delete(cmd.split(' ')[1])

        else:
            print('\'' + cmd + '\'', 'Command not found')

    def print_commands(self):
        print('List of available commands:')
        print('---------------------------')
        self.print_table_value('exit/quit', 'Closes the program')
        self.print_table_value('help', 'List all available commands')
        self.print_table_value('cls/clear', 'Clears the screen')
        self.print_table_value('show-all', 'Shows all passwords')
        self.print_table_value(
            'show <name>', 'Shows the password for that entry')
        self.print_table_value('new <name> <pass>',
                               'Creates a new password entry')
        self.print_table_value(
            'edit <name>', 'Edit an existing password entry')
        self.print_table_value('del <name>', 'Removes a password entry')
        print('')

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
        if name == 'user':
            print('Sorry, user is a reserved name!')
            return False

        self.db.new(name, password)
        return True

    def edit(self, name):
        if self.db.get(name) == None:
            print('Unable to edit:', name + '.', 'It does not exist')
            return

        # Prevents error when the user changes the user account password
        new_name = ''

        if name != 'user':
            print('Press enter to skip name edit')
            new_name = input('new name: ')

        new_pass = input('new pass: ')

        if len(new_name) == 0:
            new_name = name

        if len(new_pass) == 0 and len(new_name) == 0:
            print('Unable to edit:', name + '.', 'No values updated')
        elif len(new_pass) == 0:
            print('Error: Please enter a value for the password!')
            return

        # Commit the updated entry
        self.db.edit(name, new_name, new_pass)

    def delete(self, name):
        if self.db.get(name) == None:
            print('Unable to delete:', name + '.', 'It does not exist')
            return

        self.db.delete(name)
        print('Successfully deleted:', name)

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
