#!/usr/bin/python3

"""
A console application
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    A console application class
    """

    prompt = "(hbnb) "

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
