# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 22:01:50 2016

@author: localuser
"""

import unittest, grid_cell

class GeidCellTest(unittest.TestCase):
    """TestCase for grid cells."""

    def test_exit(self):
        """Test exit construction"""
        mycell = grid_cell.Exit()
        self.assertEqual(str(mycell), 'U')
        self.assertTrue(mycell.is_crossable())

    def test_exit_from_char(self):
        """Test exit construction"""
        mycell = grid_cell.GridCell.from_char('U')
        self.assertEqual(str(mycell), 'U')
        self.assertTrue(mycell.is_crossable())

    def test_door(self):
        """Test door construction"""
        mycell = grid_cell.Door()
        self.assertEqual(str(mycell), '.')
        self.assertTrue(mycell.is_crossable())

    def test_door_from_char(self):
        """Test door construction"""
        mycell = grid_cell.GridCell.from_char('.')
        self.assertEqual(str(mycell), '.')
        self.assertTrue(mycell.is_crossable())

    def test_empty(self):
        """Test empty cell construction"""
        mycell = grid_cell.Empty()
        self.assertEqual(str(mycell), ' ')
        self.assertTrue(mycell.is_crossable())

    def test_empty_from_char(self):
        """Test empty cell construction"""
        mycell = grid_cell.GridCell.from_char(' ')
        self.assertEqual(str(mycell), ' ')
        self.assertTrue(mycell.is_crossable())

    def test_wall(self):
        """Test wall construction"""
        mycell = grid_cell.Wall()
        self.assertEqual(str(mycell), 'O')
        self.assertFalse(mycell.is_crossable())

    def test_wall_from_char(self):
        """Test wall construction"""
        mycell = grid_cell.GridCell.from_char('O')
        self.assertEqual(str(mycell), 'O')
        self.assertFalse(mycell.is_crossable())

    def test_robot(self):
        """Test robot construction"""
        mycell = grid_cell.Robot()
        self.assertEqual(str(mycell), '*')
        self.assertFalse(mycell.is_crossable())

    def test_robot_from_char(self):
        """Test robot construction"""
        mycell = grid_cell.GridCell.from_char('*')
        self.assertEqual(str(mycell), '*')
        self.assertFalse(mycell.is_crossable())
