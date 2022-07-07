#!/usr/bin/python3
import cmd
import sys
import shlex
import models
from models import base_model
from models import place
from models import review
from models import user
from models import state
from models import city
from models import amenity
from models import storage

"""
Setup console application
"""


classes = {"Amenity", "City", "Place", "Review", "State", "User"}


class Airbnb_Shell(cmd.Cmd):
    """.editorconfig"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance"""
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
        if line[0] != "BaseModel":
            print("** class doesn't exist **")
        instance = classes[line[0]]()
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        splitted_args = arg.split()
        current_class = None
        current_id = None
        data = storage.all()

        if len(splitted_args) >= 1:
            current_class = splitted_args[0]
        if len(splitted_args) >= 2:
            current_id = splitted_args[1]
        if current_class is None:
            print("** class name missing **")
        elif current_class not in classes:
            print("** class name missing **")
        elif current_id is None:
            print("** instance id missing **")
        elif "{}.{}".format(current_class, current_id) not in data:
            print("** no instance found **")
        else:
            print(data["{}.{}".format(current_class, current_id)])

    def do_destroy(self, arg):
        """
        Destroy an instance
        """

        splitted_args = arg.split()
        current_class = None
        current_id = None
        data = storage.all()

        if len(splitted_args) >= 1:
            current_class = splitted_args[0]
        if len(splitted_args) >= 2:
            current_id = splitted_args[1]

        data = storage.all()
        if current_class is None:
            print("** class name missing **")
        elif current_class not in classes:
            print("** class doesn't exist **")
        elif current_id is None:
            print("** instance id missing **")
        elif "{}.{}".format(current_class, current_id) not in data.keys():
            print("** no instance found **")
        else:
            del data["{}.{}".format(current_class, current_id)]
            storage.save()

    def do_all(self, arg):
        print("all")

    def do_update(self, arg):
        print("update")

    def do_quit(self, arg):
        'Command to quit the program'
        return True


if __name__ == '__main__':
    Airbnb_Shell().cmdloop()
