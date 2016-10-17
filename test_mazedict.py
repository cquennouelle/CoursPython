# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:19:24 2016

@author: cquennouelle
"""

import unittest
import mazedict

class MazedictTest(unittest.TestCase):
    """TestCase for MazeDict class."""

    def test_init(self):
        """Test default construction."""
        mymazedict = mazedict.Mazedict()
        self.assertEqual(mymazedict.size, 0)

    def test_autosearch_0(self):
        """Test for autosearch method."""
        mymazedict = mazedict.Mazedict()
        with self.assertRaises(FileNotFoundError):
            mymazedict.autosearch('erroneousrepname')

    def test_autosearch_1(self):
        """Test for autosearch method."""
        mymazedict = mazedict.Mazedict()
        mymazedict.autosearch('testmazedictempty')
        self.assertEqual(mymazedict.size, 0)

    def test_autosearch_2(self):
        """Test for autosearch method."""
        mymazedict = mazedict.Mazedict()
        mymazedict.autosearch('testmazedicttwo')
        self.assertEqual(mymazedict.size, 3)

    def test_autosearch_error(self):
        """Test autosearch with erroneous parameter type."""
        mymazedict = mazedict.Mazedict()
        with self.assertRaises(TypeError):
            mymazedict.autosearch(1)

    def test_get_item_by_string(self):
        """Test access value through a key."""
        mymazedict = mazedict.Mazedict()
        mymazedict.autosearch('testmazedicttwo')
        self.assertEqual(str(mymazedict["mini"]), "OOO\nO U\nOOO")
        self.assertEqual(mymazedict["mini"].height, 3)
        self.assertEqual(mymazedict["maze1"].height, 22)
        self.assertEqual(mymazedict["maze2"].height, 21)

    def test_get_item_by_index(self):
        """Test access value through a key."""
        mymazedict = mazedict.Mazedict()
        mymazedict.autosearch('testmazedicttwo')
        self.assertEqual(str(mymazedict[2]), "OOO\nO U\nOOO")
        self.assertEqual(mymazedict[0].height, 22)
        self.assertEqual(mymazedict[1].height, 21)
        self.assertEqual(mymazedict[2].height, 3)
