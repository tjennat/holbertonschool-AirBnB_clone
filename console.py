#!/usr/bin/python3
"""this module contains the console class"""
import cmd
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_quit(self, line):
        '''quit command'''
        return True

    def do_EOF(self, line):
        """EOF command"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not line:
            print("** class name missing **")
        else:
            class_name = line.split()[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return

            classe = globals()[class_name]
            new_instance = classe()
            new_instance.save()
            print(new_instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
