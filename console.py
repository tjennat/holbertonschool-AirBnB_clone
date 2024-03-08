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

    def check_instance(self, line):
        """retun the instance from json if the line refere to an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return None

        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return None

        instance_id = args[1]

        all_instances = storage.all()
        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in all_instances:
            print("** no instance found **")
            return None

        return all_instances[instance_key]

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id."""
        instance = self.check_instance(line)
        if instance:
            print(instance)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        instance = self.check_instance(line)

        if instance:
            class_name = instance.__class__.__name__
            instance_id = instance.id
            instance_key = f"{class_name}.{instance_id}"

            all_instances = storage.all()
            if instance_key in all_instances:
                del all_instances[instance_key]
                storage.save()
            else:
                print("** no instance found **")


    def do_all(self, line):
        """Prints all string representation of
        all instances based or not on the class name."""
        if not line:

            all_instances = storage.all()
            for instance_key, instance in all_instances.items():
                print(instance)
        else:

            class_name = line.split()[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return

            instances_of_class = [instance
                                  for key, instance in storage.all().items()
                                  if class_name in key]
            if not instances_of_class:
                print("** no instance found **")
                return

            for instance in instances_of_class:
                print(instance)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
