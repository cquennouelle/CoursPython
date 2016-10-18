# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:21:53 2016

@author: localuser
"""

from roboc import Roboc

class RobocInterface(object):
    """Class managing interaction with roboc."""

    def __init__(self, directory):
        """Construction."""
        self._roboc = Roboc(directory)

    def _print_mazelist(self):
        """Print list of available mazes to choose."""
        mazedict = self._roboc.mazedict
        for n_maze in range(mazedict.size):
            print(str(n_maze+1) + " - " + mazedict.get_name(n_maze))

    def run(self):
        """Test run roboc."""
        self._print_mazelist()
