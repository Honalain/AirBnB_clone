#!/usr/bin/python3
"""
Uniy test for console.py file using unnittest
module from python standard library
and check if console is capturing stdout into
a string input and output(IO) object
"""
import os
import sys
from io import stringIO
import unittest
from unittest.mock import create_autospec, patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from model.user import User
from models.state import State
from models.city import city
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):

    """
    unittest for the console file model
    """
    def SetUp(self):
        """
        Redirecting standard input (stdin) and standard
        output (stdout)
        """
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.err = ["**class name is missing **",
                "**class doesn't exist **",
                "**instance is missing **",
                "**no instance found **"]
        self.cls = ["BaseModel",
                "User",
                "State",
                "City",
                "place",
                "Amenity", 
                "Review"]

    def create(self, server=None):
    """
    Redirect standard input (stdin) and standard output (stdout)
    to the mock module
    """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def last_written(self, last=None):
    """ Return the last output (n) line """
        if last is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
            self.mock_stdout.write.call_args_list[-last:]))

    def quit_test(self):
    """ Quitting the command """
        cli = self.created()
        self.assertTrue(cli.onecmd("quit"))

    if __name == '__main__':
        unittest.main()
