#!/usr/bin/python3
"""this module contains the console class"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        '''quit command'''
        return True

    def do_EOF(self, line):
        """EOF command"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    if __name__ == "__main__":
        HBNBCommand().cmdloop()
