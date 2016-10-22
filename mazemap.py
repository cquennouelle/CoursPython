# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 20:15:18 2016

@author: localuser
"""
import grid_cell

class Mazemap(object):
    """Class representing a map."""

    def _load_from_string(self, string):
        """Load a grid from a string."""
        size = len(string)
        self._grid = []
        if size > 0:
            rows = string.split('\n')
            for row in rows:
                if len(row) > 0:
                    gridrow = []
                    for letter in row:
                        gridrow.append(grid_cell.GridCell.from_char(letter))
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
            sourcefile.write(self.__str__())

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
        return self.__str__()

    def _get_grid(self):
        """Access to the grid."""
        return self._grid

    def __getitem__(self, key):
        """Assess item through its key."""
        if type(key) is not tuple:
            raise TypeError
        else:
            return self._grid[key[0]][key[1]]

    def _get_height(self):
        """Get the grid heigth."""
        return len(self._grid)

    def __str__(self):
        """ Get grid as a string."""
        string = str('')
        for row in self._grid:
            for cell in row:
                string += str(cell)
            string += '\n'
        return string[0:len(string)-1]

    def get_game(self, pos):
        """Get string map + robot."""
        occupiedgrid = []
        for row in self._grid:
            occupiedgrid.append(list(row))
        occupiedgrid[int(pos[0])][int(pos[1])] = grid_cell.Robot()
        return occupiedgrid

    # Properties
    grid = property(_get_grid)
    height = property(_get_height)
