# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:19:24 2016

@author: cquennouelle
"""

import unittest
from mazedict import *

class MazedictTest(unittest.TestCase):
    """TestCase for MazeDict class."""

    def test_init(self):
        """Test default construction."""
        mazedict = Mazedict()
        self.assertEqual(mazedict.size(), 0)

    def test_autosearch_0(self):
        """Test for autosearch method."""
        mazedict = Mazedict()
        with self.assertRaises(FileNotFoundError):
            mazedict.autosearch('erroneousrepname')

    def test_autosearch_1(self):
        """Test for autosearch method."""
        mazedict = Mazedict()
        mazedict.autosearch('testmazedictempty')
        self.assertEqual(mazedict.size(), 0)

    def test_autosearch_2(self):
        """Test for autosearch method."""
        mazedict = Mazedict()
        mazedict.autosearch('testmazedicttwo')
        self.assertEqual(mazedict.size(), 2)

    def test_autosearch_error(self):
        """Test autosearch with erroneous parameter type."""
        mazedict = Mazedict()
        with self.assertRaises(TypeError):
            mazedict.autosearch(1)
