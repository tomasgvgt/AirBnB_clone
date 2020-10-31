#!/usr/bin/python3
import cmd
import shlex
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    """
    name_class = ["BaseModel"]
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
            return False
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
            return False
        elif line_arg[0] not in HBNBCommand.name_class:
            print("** class doesn't exist **")
        elif len(line_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(line_arg[0], line_arg[1]) not in models.storage.all().keys():
            print("** no instance found **")
        else:
            print(models.storage.all()["{}.{}".format(line_arg[0], line_arg[1])])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
