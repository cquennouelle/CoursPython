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
        self._mazelist = []

    def autosearch(self, dirname):
        """Look for all existing mazemap in the repository 'rep'."""
        if type(dirname) is not str:
            raise TypeError
        dirlist = os.listdir(dirname)
        dirlist.sort()
        for filename in dirlist:
            if filename.endswith(".maze"):
                pathname = os.path.join(dirname, filename)
                mazename = filename[:-5].lower()
                self._dict[mazename] = mazemap.Mazemap(filename=pathname)
        # Sort dictionary and put it in a list
        self._mazelist = []
        for key in self._dict.keys():
            self._mazelist.append(key)
        self._mazelist.sort()

    def __str__(self):
        """Get a mazedict as a string."""
        string = ''
        for key in self._dict.keys():
            string += key + '\n'
        return string[:-2]

    def __getitem__(self, key):
        """Assess item through its key."""
        if type(key) is int:
            return self._dict[self._mazelist[key]]
        else:
            return self._dict[key]

    def _get_size(self):
        """Give number of mazemaps."""
        return len(self._dict.values())

    size = property(_get_size)
    