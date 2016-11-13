# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:23:41 2016

@author: cquennouelle
"""
import os
import mazemap
from operator import itemgetter

class Mazedict(object):
    """Class representing a dictionary of mazes."""

    def __init__(self, dirname=''):
        """Construction."""
        self._dict = {}
        self._mazelist = []
        if not dirname=='':
            self._autosearch(dirname)

    def _autosearch(self, dirname):
        """Look for all existing mazemap in the repository 'rep'."""
        if not isinstance(dirname, str):
            raise TypeError
        dirlist = os.listdir(dirname)
        dirlist.sort()
        _maze_filetype='.maze'
        for filename in dirlist:
            if filename.endswith(_maze_filetype):
                pathname = os.path.join(dirname, filename)
                mazename = filename[:-len(_maze_filetype)].lower()
                self._dict[mazename] = mazemap.Mazemap(filename=pathname)
        # Sort dictionary and put it in a list
        self._mazelist = []
        for key in self._dict.items():
            self._mazelist.append(key)
        self._mazelist.sort(key=itemgetter(0))

    def __str__(self):
        """Get a mazedict as a string."""
        string = ''
        for key in self._dict.keys():
            string += key + '\n'
        return string[:-2]

    def get_name(self, index):
        """Get name of mazemap."""
        return self._mazelist[index][0]

    def __getitem__(self, key):
        """Assess item through its key."""
        if type(key) is int:
            return self._dict[self._mazelist[key][0]]
        else:
            return self._dict[key]

    def _get_size(self):
        """Give number of mazemaps."""
        return len(self._dict.values())

    size = property(_get_size)
