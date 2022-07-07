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

"""
Setup console application
"""


class Airbnb_Shell(cmd.Cmd):
    """.editorconfig"""

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
        print("show")

    def do_destroy(self, arg):
        print("destroy")

    def do_all(self, arg):
        print("all")

    def do_update(self, arg):
        print("update")

    def do_quit(self, arg):
        return True


if __name__ == '__main__':
    Airbnb_Shell().cmdloop()
