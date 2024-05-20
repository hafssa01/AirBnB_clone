#!/usr/bin/python3

"""HBNB command-line interpreter.

And this is a list of all used modules in this section
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    """HBNB command interpreter class.

    This class provides a simple command-line interface for interacting
    with the HBNB application (if applicable).
    """

    prompt = '(hbnb) '
    classList = ["BaseModel"]

    def do_EOF(self, line):
        """Handle EOF to exit the program."""
        print()
        return True

    def do_quit(self, line):
        """Quits the HBNB command interpreter."""
        return True

    def emptyline(self):
        """Ignores empty lines."""
        pass

    def help_EOF(self):
        print('End Of File (Ctrl-D) to close the console')

    def help_quit(self):
        """Print help for the EOF command."""
        print('Quit command to exit the program')

    # CRUD operations

    def do_create(self, line):
        """
        create: Creates a new instance of BaseModel,
        Saves it (to the JSON file) and prints the unique id
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
        elif len(args) == 1:
            if args[0] not in self.classList:
                print("** class doesn't exist **")
            else:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classList:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id is missing **")
        else:
            dict = storage.all()  # retrieves all objects from the storage

            key = "{}.{}".format(args[0], args[1])  # constructring a key
            if key in dict:  # checks if instance exists in returned dict
                print(dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
         Deletes an instance based on the class name and id
         Saves the change into the JSON file).
        """

        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classList:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id is missing **")
        else:
            dict = storage.all()  # retrieves all objects from the storage

            key = "{}.{}".format(args[0], args[1])
            if key in dict:
                del dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        Based or not on the class name
        """
        dict = storage.all()
        args = line.split()

        if len(args) == 0:
            for key, value in dict.items():
                print(str(value))
        elif args[0] not in self.classList:
            print("** class doesn't exist **")
        else:
            for key, value in dict.items():
                if key.split('.')[0] == args[0]:
                    print(str(value))

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        By adding or updating attribute (save the change into the JSON file)
        """

        args = line.split()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classList:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id is missing **")
        else:
            dict = storage.all()

            key = "{}.{}".format(args[0], args[1])
            if key not in dict:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:

                # retrieves an object associated to
                # specefic class name w/ an unique id

                obj = dict[key]

                att_name = args[2]
                att_value = args[3]

                # Handles type's error
                try:
                    att_value = eval(att_value)  # evaluating this string val
                except Exception:
                    pass
                # Updates the object's attribute
                # to a new given value
                setattr(obj, att_name, att_value)

                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
