# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:23:41 2016

@author: cquennouelle
"""
import os
import mazemap

class Mazedict(object):
    """Class representing a dictionary of mazes."""

    def __init__(self):
        """Construction."""
        self._dict = {}

    def autosearch(self, repname):
        """Look for all existing mazemap in the repository 'rep'."""
        if type(repname) is not str:
            raise TypeError
        dirlist = os.listdir(repname)
        for filename in dirlist:
            if filename.endswith(".maze"):
                pathname = os.path.join(repname, filename)
                mazename = filename[:-4].lower()
                self._dict[mazename] = mazemap.Mazemap(filename=pathname)

    def size(self):
        """Give number of mazemaps."""
        return len(self._dict.values())
