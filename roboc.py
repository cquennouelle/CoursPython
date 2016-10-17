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

    currentmaze = property(_get_currentmaze)
