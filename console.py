#!/usr/bin/python3
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    """
    name_class = ["BaseModel", "User", "State", "City", "Amenity",
    "Place", "Review"]
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Quit command to exit the program with (ctrl + "D")
        """
        # CHECK END OF LINE CTRL + D
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """ Command to creates a new instance
        """
        # tokens to data into line
        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                line_arg = shlex.split(line)
                new_Create = eval(line_arg[0])()  # REVISAR
                new_Create.save()
                print(new_Create.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, line):
        """[summary]
        """
        line_arg = line.split()
        if len(line_arg) == 0:
            print("** class name missing **")
        elif line_arg[0] not in HBNBCommand.name_class:
            print("** class doesn't exist **")
        elif len(line_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(
                line_arg[0], line_arg[1]) not in models.storage.all().keys():
            print("** no instance found **")
        else:
            print(models.storage.all()["{}.{}".format(
                line_arg[0], line_arg[1])])

    def do_destroy(self, line):
        line_arg = line.split()
        if len(line_arg) == 0:
            print("** class name missing **")
        elif line_arg[0] not in HBNBCommand.name_class:
            print("** class doesn't exist **")
        elif len(line_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(
                line_arg[0], line_arg[1]) not in models.storage.all().keys():
            print("** no instance found **")
        else:
            del models.storage.all()["{}.{}".format(line_arg[0], line_arg[1])]
            models.storage.save()

    def do_all(self, line):
        instances_list = []
        if len(line) == 0:
            for key, value in models.storage.all().items():
                instances_list.append(str(value))
            print(instances_list)
            """
            OTHER WAY
            print([str(v) for v in storage.all().values()])
            """
        else:
            if line not in HBNBCommand.name_class:
                print("** class doesn't exist **")
            else:
                for key, value in models.storage.all().items():
                    if line in key:  # OR key.startswith(line)
                        instances_list.append(str(value))
                print(instances_list)

    def do_update(self, line):
        line_arg = shlex.split(line)
        if len(line_arg) < 1:
            print("** class name missing **")
        elif line_arg[0] not in HBNBCommand.name_class:
            print("** class doesn't exist **")
        elif len(line_arg) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(
                line_arg[0], line_arg[1]) not in models.storage.all().keys():
            print("** no instance found **")
        elif len(line_arg) < 3:
            print("** attribute name missing **")
        elif len(line_arg) < 4:
            print("** value missing **")
        else:
            key = line_arg[0] + "." + line_arg[1]
            setattr(models.storage.all()[key], line_arg[2], line_arg[3])
            models.storage.save()

    def default(self, line):
        my_line = line.split(".")
        if len(my_line) > 1:
            if my_line[1] == "all()":
                self.do_all(my_line[0])
            elif my_line[1] == "count()":
                if my_line[0] in HBNBCommand.name_class:
                    count = 0
                    for key in models.storage.all():
                        if my_line[0] in key:
                            count += 1
                    print(count)
                else:
                    print("** class doesn't exist **")
            elif my_line[1][:5] == "show(" and my_line[1][-1] == ")":
                class_and_id = my_line[0] + " " + my_line[1][5:-1]
                self.do_show(class_and_id)
            elif my_line[1][:8] == "destroy(" and my_line[1][-1] == ")":
                class_and_id = my_line[0] + " " + my_line[1][9:-2]
                self.do_destroy(class_and_id)
            elif my_line[1][:7] == "update(" and my_line[1][-1] == ")":
                clid_aux = my_line[1][7:-1].split()
                """if len(clid_aux) > 2:
                    class_and_id = my_line[0] + " " + clid_aux[0] + " " + clid_aux[1] + " " + clid_aux[2]
                    self.do_update(class_and_id)"""
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
