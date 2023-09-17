#!usr/bin/python3
"""console for AirBnb clone project"""

import cmd
import json
import re
import sys
from models.review import Review
from shlex import split
from models.amenity import Amenity
from models import storage
from models.place import Place
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.state import State


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)"""
        print()  # Print a newline before exiting
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
