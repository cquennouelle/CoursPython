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

    def test_place_robot(self):
        """Test method to place a robot in the maze."""
        rob = roboc.Roboc('testmazedicttwo')
        rob.select_maze(1)
        self.assertEqual(rob.robot_place, (1, 1))

    def test_move_south(self):
        """Test method to move robot one cell south."""
        rob = roboc.Roboc('testmazedicttwo')
        rob.select_maze(1)
        rob.move_south(1)
        self.assertEqual(rob.robot_place, (2, 1))

    def test_move_south_5(self):
        """Test method to move robot one cell south."""
        rob = roboc.Roboc('testmazedicttwo')
        rob.select_maze(1)
        rob.move_south(4)
        self.assertEqual(rob.robot_place, (5, 1))
        rob.move_south(1)
        self.assertEqual(rob.robot_place, (5, 1))

    def test_move_east(self):
        """Test method to move robot one cell east."""
        rob = roboc.Roboc('testmazedicttwo')
        rob.select_maze(1)
        rob.move_south(3)
        rob.move_east(1)
        self.assertEqual(rob.robot_place, (4, 2))
        rob.move_east(2)
        self.assertEqual(rob.robot_place, (4, 3))

    def test_move_west(self):
        """Test method to move robot one cell west."""
        rob = roboc.Roboc('testmazedicttwo')
        rob.select_maze(1)
        rob.move_south(3)
        rob.move_east(2)
        rob.move_west(1)
        self.assertEqual(rob.robot_place, (4, 2))
        rob.move_west(3)
        self.assertEqual(rob.robot_place, (4, 1))

    def test_move_north(self):
        """Test method to move robot one cell north."""
        rob = roboc.Roboc('testmazedicttwo')
        rob.select_maze(1)
        rob.move_south(3)
        rob.move_east(2)
        rob.move_north(1)
        self.assertEqual(rob.robot_place, (3, 3))
        rob.move_north(3)
        self.assertEqual(rob.robot_place, (1, 3))

    def test_game(self):
        """Test method to display game."""
        rob = roboc.Roboc('testmazedicttwo')
        rob.select_maze(1)
        self.assertEqual(str(rob.game), 'OUOOOOOOOOOOOOOOOOOOOOO\n'
            + 'O*O O O   O           O\n'
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
        rob.move_south(3)
        self.assertEqual(str(rob.game), 'OUOOOOOOOOOOOOOOOOOOOOO\n'
            + 'O O O O   O           O\n'
            + 'O O O O   O           O\n'
            + 'O O . OO.OO           O\n'
            + 'O*. O             OOOOO\n'
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

    def test_is_won(self):
        """Test for wining game."""
        rob = roboc.Roboc('testmazedicttwo')
        rob.select_maze('mini')
        self.assertFalse(rob.is_won())
        rob.move_east(1)
        self.assertTrue(rob.is_won())