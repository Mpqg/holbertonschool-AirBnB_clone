#!/usr/bin/python3
import cmd

"""
Setup console application
"""


classes = {"Amenity", "City", "Place", "Review", "State", "User"}

class Airbnb_Shell(cmd.Cmd):
    """.editorconfig"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        print("create")

    def do_show(self, arg):
        splitted_args = arg.split()
        current_class = None
        current_id = None

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

    def do_destroy(self, arg):
        print("destroy")

    def do_all(self, arg):
        print("all")

    def do_update(self, arg):
        print("update")

    def do_quit(self, arg):
        'Command to quit the program'
        return True


if __name__ == '__main__':
    Airbnb_Shell().cmdloop()
