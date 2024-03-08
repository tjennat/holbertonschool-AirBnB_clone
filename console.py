#!/usr/bin/python3
"""this module contains the console class"""
import cmd
from models.base_model import BaseModel
from models import storage



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

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        # Chargez l'instance à partir du fichier JSON
        all_instances = storage.all()
        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in all_instances:
            print("** no instance found **")
            return

        print(all_instances[instance_key])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
