#!/usr/bin/python3

"""
A console application
"""


import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    A console application class
    """

    prompt = "(hbnb) "
    command_list = ["BaseModel", "User", "State", "City"]

    def emptyline(self):
        """
        Handles the empty line prompt
        """
        return

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True
    def help_quit(self):
        """
        Quit command to exit the program (help)
        """
        print("{}".format("Quit command to exit the program"))
        print()

    def do_EOF(self, line):
        """
        Quit command on End of File
        """
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        """
        command = self.parseline(line)[0]
        if command is None:
            print("** class name missing **")
        elif command not in self.command_list:
            print("** class doesn't exist **")
        else:
            new_obj = eval(command)()
            new_obj.save()
            print(new_obj.id)
    def help_create(self):
        """
        Creates a new instance of `BaseModel` (help)
        """
        print("{}".format("Creates a new instance of BaseModel"))

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        class_name = self.parseline(line)[0]
        class_id = self.parseline(line)[1]
        if class_name is None:
            print("** class name missing **")
        elif class_name not in self.command_list:
            print("** class doesn't exist **")
        elif class_id is None or class_id == "":
            print("** instance id missing **")
        else:
            new_inst = models.storage.all().get(class_name + "." + class_id)
            if new_inst is None:
                print("** no instance found **")
            else:
                print(new_inst)
    def help_show(self):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        print("{}".format("Prints the string representation based on class"))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
