import os

class Interpreter:
    def __init__(self):
        pass


    def execCommand(self, cmd):
        if 'exit' in cmd or 'quit' in cmd:
            return 0
        elif 'help' in cmd:
            self.print_commands()
        elif 'cls' in cmd or 'clear' in cmd:
            self.clear_screen()
        elif 'show-all' in cmd or '--show-all' in cmd:
            pass

        else:
            print('\'' + cmd + '\'', 'Command not found')


    def print_commands(self):
        print('List of available commands:')
        print('---------------------------')
        print('exit/quit                Closes the program')
        print('help                     List all available commands')
        print('cls/clear                Clears the screen')
        print('show-all                 Shows all passwords')
        print('show <name>              Shows the password for that entry')
        print('new <name> <pass>        Creates a new password entry')
        # This command will ask for the new passfor and password
        # If passfor is empty it will not be updated, but the pass will
        print('edit <name>              Edit an existing password entry')
        print('del <name>               Removes a password entry')


    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    def show_all(self):
        pass

    
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