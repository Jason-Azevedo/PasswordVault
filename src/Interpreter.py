
class Interpreter:
    def __init__(self):
        pass

    def execCommand(self, cmd):
        print(cmd)

    def Interpret(self):
        print('Enter command below, help to list all commands, exit/quit to close program')
        while True:
            try:
                cmd = input('> ')
            except EOFError:
                print('EOF Error occured')
            except KeyboardInterrupt:
                break
            
            self.execCommand(cmd)