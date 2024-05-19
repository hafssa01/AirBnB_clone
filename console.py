#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):

    """HBNB command interpreter class."""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Handle EOF to exit the program"""
        print()
        return True

    def do_quit(self, line):
       """Quits the command interpreter."""
       return True

    def emptyline(self):
        """Ignores empty lines."""
        pass

    def help_EOF(self):
        print('End Of File (Ctrl-D) to close the console')

    def help_quit(self):
        """Print help for the EOF command."""
        print('Quit command to exit the program')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
