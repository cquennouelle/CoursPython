# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 20:15:18 2016

@author: localuser
"""

class Mazemap:
    """Class representing a map."""

    def _load_from_string(self, string):
        """Load a grid from a string."""
        size = len(string)
        self._grid = []
        if size > 0:
            rows = string.split(sep='\n')
            for row in rows:
                if len(row) > 0:
                    gridrow = []
                    for letter in row:
                        gridrow.append(letter)
                    self._grid.append(gridrow)

    def _load_from_file(self, filename):
        """Get the string from the file and load it to a the grid."""
        with open(filename, 'r') as sourcefile:
            mazestring = str(sourcefile.read())
            mazestring.strip()
            self._load_from_string(mazestring)

    def save_to_file(self, filename):
        """Save maze in a file."""
        with open(filename, 'w') as sourcefile:
            sourcefile.write(self.get_as_string())

    def __init__(self, string='', filename=''):
        if type(string) is not str:
            raise TypeError("Requires a string to build a maze.")
        if string == '':
            if filename == '':
                self._grid = []
            else:
                self._load_from_file(filename)
        else:
            self._load_from_string(string)

    def __repr__(self):
        return "Maze :\n" + self.get_as_string()

    def get_as_string(self):
        """ Get grid as a string."""
        string = str('')
        for row in self._grid:
            for col in row:
                string += col
            string += '\n'
        return string[0:len(string)-1]
