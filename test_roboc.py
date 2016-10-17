# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:20:45 2016

@author: localuser
"""

import unittest
import roboc

class RobocTest(unittest.TestCase):
    """Test class Roboc."""

    def test_init(self):
        """Test default construction."""
        rob = roboc.Roboc('testmazedicttwo')
        self.assertEqual(rob._mazedict.size, 3)

    def test_get_current_maze(self):
        """Test for selecting maze."""
        rob = roboc.Roboc('testmazedicttwo')
        mymaze = rob.currentmaze
        self.assertEqual(str(mymaze),'OOO\nO U\nOOO')

#    def test_print_mazelist(self):
#        """Test for 
