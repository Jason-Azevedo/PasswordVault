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
        print('{:<25} {:<20}'.format('exit/quit', 'Closes the program'))
        print('{:<25} {:<20}'.format('help', 'List all available commands'))
        print('{:<25} {:<20}'.format('cls/clear', 'Clears the screen'))
        print('{:<25} {:<20}'.format('show-all', 'Shows all passwords'))
        print('{:<25} {:<20}'.format('show <name>',
                                     'Shows the password for that entry'))
        print('{:<25} {:<20}'.format('new <name> <pass>',
                                     'Creates a new password entry'))
        print('{:<25} {:<20}'.format('show <name>',
                                     'Shows the password for that entry'))
        # This command will ask for the new passfor and password
        # If passfor is empty it will not be updated, but the pass will
        print('{:<25} {:<20}'.format('edit <name>',
                                     'Edit an existing password entry'))
        print('{:<25} {:<20}'.format('del <name>',
                                     'Removes a password entry'))

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def show_all(self):
        passEntries = self.db.get_all()
        print('{:<25} {:<20}'.format('Entry', 'Password'))

        for entry in passEntries:
            print('{:<25} {:<20}'.format(entry[0], entry[1]))

    def show(self, name):
        pass

    def new(self, name, password):
        pass

    def edit(self, name):
        pass

    def delete(self, name):
        pass

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
