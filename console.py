#!/usr/bin/python3
import cmd

"""
Setup console application
"""


class Airbnb_Shell(cmd.Cmd):
    """.editorconfig"""

    def do_create(self, arg):
        print("create")

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
