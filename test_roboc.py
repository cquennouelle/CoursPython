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
        self.assertEqual(str(mymaze), 'OOO\nO U\nOOO')

    def test_select_maze_by_name(self):
        """Test for selecting maze."""
        rob = roboc.Roboc('testmazedicttwo')
        rob.select_maze('maze2')
        self.assertEqual(str(rob.currentmaze), 'OUOOOOOOOOOOOOOOOOOOOOO\n'
            + 'O O O O   O           O\n'
            + 'O O O O   O           O\n'
            + 'O O . OO.OO           O\n'
            + 'O . O             OOOOO\n'
            + 'O O O    OOOOOOOOOO   O\n'
            + 'OOOOOOOO.O            O\n'
            + 'O                     O\n'
            + 'O                     O\n'
            + 'OOOOOOOOOOOOOOOOOOO.OOO\n'
            + 'O                     O\n'
            + 'OOOOOOOO.OOOOOOOOOOOOOO\n'
            + 'O                 O   O\n'
            + 'OOOOOOOOOOOOOOO.OOOOO.O\n'
            + 'O                     O\n'
            + 'OOOOOOOOOOOOOOOOOOOOO O\n'
            + 'O                     O\n'
            + 'O                     O\n'
            + 'O                     O\n'
            + 'O                     O\n'
            + 'OOOOOOOOOOOOOOOOOOOOOOO')
        rob.select_maze('mini')
        self.assertEqual(str(rob.currentmaze), 'OOO\nO U\nOOO')

    def test_select_maze_type_error(self):
        """Test for selecting maze."""
        rob = roboc.Roboc('testmazedicttwo')
        with self.assertRaises(TypeError):
            rob.select_maze(1.5)

    def test_select_maze_by_index(self):
        """Test for selecting maze by its index."""
        rob = roboc.Roboc('testmazedicttwo')
        rob.select_maze(1)
        self.assertEqual(str(rob.currentmaze), 'OUOOOOOOOOOOOOOOOOOOOOO\n'
            + 'O O O O   O           O\n'
            + 'O O O O   O           O\n'
            + 'O O . OO.OO           O\n'
            + 'O . O             OOOOO\n'
            + 'O O O    OOOOOOOOOO   O\n'
            + 'OOOOOOOO.O            O\n'
            + 'O                     O\n'
            + 'O                     O\n'
            + 'OOOOOOOOOOOOOOOOOOO.OOO\n'
            + 'O                     O\n'
            + 'OOOOOOOO.OOOOOOOOOOOOOO\n'
            + 'O                 O   O\n'
            + 'OOOOOOOOOOOOOOO.OOOOO.O\n'
            + 'O                     O\n'
            + 'OOOOOOOOOOOOOOOOOOOOO O\n'
            + 'O                     O\n'
            + 'O                     O\n'
            + 'O                     O\n'
            + 'O                     O\n'
            + 'OOOOOOOOOOOOOOOOOOOOOOO')
