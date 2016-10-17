# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:17:58 2016

@author: cquennouelle
"""

import mazedict

class Roboc(object):
    """Class containing the game Roboc."""

    def __init__(self, directory='mazemaps'):
        """Construction."""
        self._mazedict = mazedict.Mazedict()
        self._mazedict.autosearch(directory)
        self._currentmaze = self._mazedict['mini']

    def _get_currentmaze(self):
        """Get the selected maze."""
        return self._currentmaze

    def select_maze(self, maze='mini'):
        """Select a maze by its name."""
        if type(maze) is str:
            self._currentmaze = self._mazedict[maze]
        elif type(maze) is int:
            self._currentmaze = self._mazedict[maze]
        else:
            raise TypeError

    currentmaze = property(_get_currentmaze)
