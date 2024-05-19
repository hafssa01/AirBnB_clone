#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):

    """documentation"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True

    do_quit = do_EOF

    def emptyline(self):
        pass

    def help_EOF(self):
        print('End Of File to close the console')

    def help_quit(self):
        print('Quit command to exit the program')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
