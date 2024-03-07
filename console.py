#!/usr/bin/python3
"""this module contains the console class"""
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class for the console"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        '''quit command'''
        return True

    def do_EOF(self, line):
        """EOF command"""
        print()
        return True

    def help_quit(self):
        """help quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """help EOF command"""
        print("EOF command to exit the program")

    def emptyline(self):
        """empty line"""
        pass

    if __name__ == "__main__":
        HBNBCommand().cmdloop()
