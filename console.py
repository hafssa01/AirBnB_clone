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

    
    """CRUD OPs"""

    def __init__(self):
        super().__init__() #construtor superclass first 
        self.users = {} #a dictionary

    
    def do_create(self, line):
        """Create a new user Syntax : create <digit> <name>"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            self.users[digit] = name
            print('A user is created successfully')
        else:
            print('Invalid input')
    
    def do_read(self, line):
        """Reads and displays all our created inputs(users)"""
        print("list of users:")
        if self.users:
            for digit, name in self.users.items():
                print(f"ID: {digit} -> Name: {name}")
        else:
            print('Nada')
    
    def do_update(self, line):
        """Updates a given user input"""
        args = line.split()
        if len(args) == 2:
            """Tokenization of args"""
            digit, name = args
            if digit in self.users.items:
                self.users[digit] = name #another creation upon the same id
                print(f"User's id {digit} is updated successfuly")
            else:
                print("Invalid id")
    
    def do_delete(self, line):
        """Destroy a given user input"""
        
        if line in self.users:
            del self.users[line]#another  creation upon the same id
            print(f"User's id {line} is deleted successfuly")
        else:
            print("Invalid id")
    
       
if __name__ == '__main__':
    HBNBCommand().cmdloop()