#!/usr/bin/python3
"""This is going to be my class for storing some files"""

import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """gonna return the dictionnary"""
        return self.__objects
    
    def new(self, obj):
        """gonna sets the obj with key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes"""
        from models import base_model
        dict_module = {"BaseModel" : base_model}

        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name in dict_module :
                        module_name = dict_module[class_name]
                    class_ = getattr(module_name, class_name)
                    FileStorage.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass
