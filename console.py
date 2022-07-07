#!/usr/bin/python3
import cmd
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

"""
Setup console application
"""


classes = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


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
        splitted_args = arg.split()
        current_class = None

        if len(splitted_args) >= 1:
            current_class = splitted_args[0]

        if current_class not in classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if current_class == obj.__class__.__name__:
                    objl.append(obj.__str__())
                else:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(sef, arg):
        splitted_args = arg.split()
        current_class = None

        if len(splitted_args) >= 1:
            current_class = splitted_args[0]

        count = 0
        for obj in storage.all().values():
            if current_class == obj.__class__.__name__:
                count += 1
        print(count)

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_update(self, arg):
        """
        Update an instance
        """
        argl = arg.split()
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    Airbnb_Shell().cmdloop()
