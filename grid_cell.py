# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:49:18 2016

@author: localuser
"""

class GridCell(object):
    """Class representing a maze cell."""

    def __init__(self):
        """Construction."""
        self._symbol = 'X'
        self._is_crossable = False

    def __str__(self):
        """Method to print a cell."""
        return self._symbol

    def is_crossable(self):
        """Method to know if the robot can go on this cell."""
        return self._is_crossable

    def from_char(character):
        """Factory method."""
        if type(character) is not str:
            raise TypeError
        if character == 'U':
            return Exit()
        if character == '.':
            return Door()
        elif character == 'O':
            return Wall()
        elif character == ' ':
            return Empty()
        elif character == '*':
            return Robot()
        else:
            print('Received \'{}\' as parameter.'.format(character))
            raise ValueError

class Exit(GridCell):
    """Class representing a door."""
    def __init__(self):
        """Construction."""
        self._symbol = 'U'
        self._is_crossable = True

class Door(GridCell):
    """Class representing a door."""
    def __init__(self):
        """Construction."""
        self._symbol = '.'
        self._is_crossable = True

class Empty(GridCell):
    """Class representing an empty cell."""
    def __init__(self):
        """Construction."""
        self._symbol = ' '
        self._is_crossable = True

class Wall(GridCell):
    """Class representing a wall."""
    def __init__(self):
        """Construction."""
        self._symbol = 'O'
        self._is_crossable = False

class Robot(GridCell):
    """Class representing a robot."""
    def __init__(self):
        """Construction."""
        self._symbol = '*'
        self._is_crossable = False
