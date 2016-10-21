# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:29:14 2016

@author: cquennouelle
"""

import unittest
from mazemap import Mazemap
from grid_cell import Door, Wall, Empty, Robot, Exit

class MazemapTest(unittest.TestCase):
    """Test class MazeMap."""

    def test_init_with_parameters_error(self):
        """Test construction error when wrong parameter type."""
        with self.assertRaises(TypeError):
            _ = Mazemap(1)

    def test_init_1(self):
        """Test for empty construction."""
        mymap = Mazemap()
        self.assertEqual(mymap.grid, [])

    def test_init_2(self):
        """Test construction from an empty string."""
        mymap = Mazemap('')
        self.assertEqual(mymap.grid, [])

    def test_init_3(self):
        """Test construction from a string."""
        mymap = Mazemap('OOO\nO U\nOOO')
        self.assertTrue(type(mymap.grid[0][0]) is Wall)
        self.assertTrue(type(mymap.grid[0][1]) is Wall)
        self.assertTrue(type(mymap.grid[0][2]) is Wall)
        self.assertTrue(type(mymap.grid[1][0]) is Wall)
        self.assertTrue(type(mymap.grid[1][1]) is Empty)
        self.assertTrue(type(mymap.grid[1][2]) is Exit)
        self.assertTrue(type(mymap.grid[2][0]) is Wall)
        self.assertTrue(type(mymap.grid[2][1]) is Wall)
        self.assertTrue(type(mymap.grid[2][2]) is Wall)

    def test_str(self):
        """Test method get_as_string."""
        string = 'OOO\nO U\nOOO'
        mymap = Mazemap(string)
        self.assertEqual(mymap.__str__(), string)

    def test_init_from_file(self):
        """Test construction from a file."""
        mymap = Mazemap(filename="LoadMazeFromFile.test")
        self.assertTrue(type(mymap.grid[0][0]) is Wall)
        self.assertTrue(type(mymap.grid[0][1]) is Wall)
        self.assertTrue(type(mymap.grid[0][2]) is Wall)
        self.assertTrue(type(mymap.grid[1][0]) is Wall)
        self.assertTrue(type(mymap.grid[1][1]) is Empty)
        self.assertTrue(type(mymap.grid[1][2]) is Exit)
        self.assertTrue(type(mymap.grid[2][0]) is Wall)
        self.assertTrue(type(mymap.grid[2][1]) is Wall)
        self.assertTrue(type(mymap.grid[2][2]) is Wall)

    def test_save_file(self):
        """Test saving mazemap in a file."""
        mymap = Mazemap('OOO\nO U\n.OO')
        mymap.save_to_file('SaveMaze.test')
        mymap2 = Mazemap(filename="SaveMaze.test")
        self.assertTrue(type(mymap2.grid[0][0]) is Wall)
        self.assertTrue(type(mymap2.grid[0][1]) is Wall)
        self.assertTrue(type(mymap2.grid[0][2]) is Wall)
        self.assertTrue(type(mymap2.grid[1][0]) is Wall)
        self.assertTrue(type(mymap2.grid[1][1]) is Empty)
        self.assertTrue(type(mymap2.grid[1][2]) is Exit)
        self.assertTrue(type(mymap2.grid[2][0]) is Door)
        self.assertTrue(type(mymap2.grid[2][1]) is Wall)
        self.assertTrue(type(mymap2.grid[2][2]) is Wall)

    def test_get_height(self):
        """Test method to get height."""
        mymap = Mazemap('OOO\nO U\nOOO')
        self.assertEqual(mymap.height, 3)
        mymap = Mazemap('OO\nOO')
        self.assertEqual(mymap.height, 2)

    def test_get_cell(self):
        """Test method to read a cell."""
        mymap = Mazemap('OOO\nO U\nOOO')
        self.assertTrue(type(mymap.grid[0][0]) is Wall)
        self.assertTrue(type(mymap.grid[0][1]) is Wall)
        self.assertTrue(type(mymap.grid[0][2]) is Wall)
        self.assertTrue(type(mymap.grid[1][0]) is Wall)
        self.assertTrue(type(mymap.grid[1][1]) is Empty)
        self.assertTrue(type(mymap.grid[1][2]) is Exit)
        self.assertTrue(type(mymap.grid[2][0]) is Wall)
        self.assertTrue(type(mymap.grid[2][1]) is Wall)
        self.assertTrue(type(mymap.grid[2][2]) is Wall)

    def test_place_robot(self):
        """Test method to place robot."""
        mymap = Mazemap('OOO\nO U\nOOO')
        mygame = mymap.get_game((1, 1))
        self.assertTrue(type(mygame[0][1]) is Wall)
        self.assertTrue(type(mygame[0][2]) is Wall)
        self.assertTrue(type(mygame[1][0]) is Wall)
        self.assertTrue(type(mygame[1][1]) is Robot)
        self.assertTrue(type(mygame[1][2]) is Exit)
        self.assertTrue(type(mygame[2][0]) is Wall)
        self.assertTrue(type(mygame[2][1]) is Wall)
        self.assertTrue(type(mygame[2][2]) is Wall)
