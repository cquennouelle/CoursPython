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
        self.assertTrue(isinstance(mymap.grid[0][0], Wall))
        self.assertTrue(isinstance(mymap.grid[0][1], Wall))
        self.assertTrue(isinstance(mymap.grid[0][2], Wall))
        self.assertTrue(isinstance(mymap.grid[1][0], Wall))
        self.assertTrue(isinstance(mymap.grid[1][1], Empty))
        self.assertTrue(isinstance(mymap.grid[1][2], Exit))
        self.assertTrue(isinstance(mymap.grid[2][0], Wall))
        self.assertTrue(isinstance(mymap.grid[2][1], Wall))
        self.assertTrue(isinstance(mymap.grid[2][2], Wall))

    def test_str(self):
        """Test method get_as_string."""
        string = 'OOO\nO U\nOOO'
        mymap = Mazemap(string)
        self.assertEqual(mymap.__str__(), string)

    def test_equal(self):
        """Test method equals."""
        string = 'OOO\nO U\nOOO'
        mymap = Mazemap(string)
        string2 = 'OOOO\nO  U\nO  O\nOOOO'
        mymap2 = Mazemap(string2)
        self.assertFalse(mymap == string)
        self.assertFalse(mymap == mymap2)
        mymap3 = Mazemap(string)
        self.assertTrue(mymap == mymap3)

    def test_init_from_file(self):
        """Test construction from a file."""
        mymap = Mazemap(filename="LoadMazeFromFile.test")
        self.assertTrue(isinstance(mymap.grid[0][0], Wall))
        self.assertTrue(isinstance(mymap.grid[0][1], Wall))
        self.assertTrue(isinstance(mymap.grid[0][2], Wall))
        self.assertTrue(isinstance(mymap.grid[1][0], Wall))
        self.assertTrue(isinstance(mymap.grid[1][1], Empty))
        self.assertTrue(isinstance(mymap.grid[1][2], Exit))
        self.assertTrue(isinstance(mymap.grid[2][0], Wall))
        self.assertTrue(isinstance(mymap.grid[2][1], Wall))
        self.assertTrue(isinstance(mymap.grid[2][2], Wall))

    def test_save_file(self):
        """Test saving mazemap in a file."""
        mymap = Mazemap('OOO\nO U\n.OO')
        mymap.save_to_file('SaveMaze.test')
        mymap2 = Mazemap(filename="SaveMaze.test")
        self.assertTrue(isinstance(mymap2.grid[0][0], Wall))
        self.assertTrue(isinstance(mymap2.grid[0][1], Wall))
        self.assertTrue(isinstance(mymap2.grid[0][2], Wall))
        self.assertTrue(isinstance(mymap2.grid[1][0], Wall))
        self.assertTrue(isinstance(mymap2.grid[1][1], Empty))
        self.assertTrue(isinstance(mymap2.grid[1][2], Exit))
        self.assertTrue(isinstance(mymap2.grid[2][0], Door))
        self.assertTrue(isinstance(mymap2.grid[2][1], Wall))
        self.assertTrue(isinstance(mymap2.grid[2][2], Wall))

    def test_get_height(self):
        """Test method to get height."""
        mymap = Mazemap('OOO\nO U\nOOO')
        self.assertEqual(mymap.height, 3)
        mymap = Mazemap('OO\nOO')
        self.assertEqual(mymap.height, 2)

    def test_col_range(self):
        """Test Method to get number of rows."""
        string = 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n'+ \
            'O . O O   O                                           O\n' + \
            'OOO O O   O       O OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOO\n' + \
            'O O O OO.OO       O  O                           OO   O\n' + \
            'O . O             OOOO             O              OOO O\n' + \
            'O O O    OOOOOOOOOO                O                  O\n' + \
            'O OOOOOO.O              OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n' + \
            'O        O              OUO                           O\n' + \
            'O        O              O O     OOOOOOOOOOOOOOOOOOOOOOO\n' + \
            'OOOOOOOOOOOOOOOOOOO.OO OO O     OOOOOOOOOOOOOOOOO      \n' + \
            'O                      O  O                     O      \n' + \
            'OOOOOOOO.OOOOOOOOOOOOO O.OOOOOOOOOOOOOOOOOO.OOO.OOOOO.O\n' + \
            'O          O      O    O  O              O   O        O\n' + \
            'OOOOOOOOOOOOO.O.OOOOO. OO OOOOOOOOOO     O   O        O\n' + \
            'O             O        O                 O   O        O\n' + \
            'OOOOO.OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO.OOOOO.OOOO.OOOOOOO\n' + \
            'O                                  O         O  O      \n' + \
            'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO   O         O  O      \n' + \
            '                               O  OOOOOOOOOOO   OOOOOOO\n' + \
            '                               O                      O\n' + \
            '                               OOOOOOOOOOOOOOOOOOOOOOOO'
        mymap = Mazemap(string)
        self.assertEqual(mymap.height, 21)
        self.assertEqual(mymap.col_range(0), (0, 54))
        self.assertEqual(mymap.col_range(17), (0, 48))
        self.assertEqual(mymap.col_range(18), (31, 54))
        
    def test_col_range_mini(self):
        """Test Method to get number of rows."""
        string = 'OOO\nO U\nOOO'
        mymap = Mazemap(string)
        self.assertEqual(mymap.height, 3)
        self.assertEqual(mymap.col_range(0), (0, 2))
        self.assertEqual(mymap.col_range(1), (0, 2))
        self.assertEqual(mymap.col_range(2), (0, 2))

    def test_get_cell(self):
        """Test method to read a cell."""
        mymap = Mazemap('OOO\nO U\nOOO')
        self.assertTrue(isinstance(mymap.grid[0][0], Wall))
        self.assertTrue(isinstance(mymap.grid[0][1], Wall))
        self.assertTrue(isinstance(mymap.grid[0][2], Wall))
        self.assertTrue(isinstance(mymap.grid[1][0], Wall))
        self.assertTrue(isinstance(mymap.grid[1][1], Empty))
        self.assertTrue(isinstance(mymap.grid[1][2], Exit))
        self.assertTrue(isinstance(mymap.grid[2][0], Wall))
        self.assertTrue(isinstance(mymap.grid[2][1], Wall))
        self.assertTrue(isinstance(mymap.grid[2][2], Wall))

    def test_place_robot(self):
        """Test method to place robot."""
        mymap = Mazemap('OOO\nO U\nOOO')
        mygame = mymap.get_game((1, 1))
        self.assertTrue(isinstance(mygame[0][1], Wall))
        self.assertTrue(isinstance(mygame[0][2], Wall))
        self.assertTrue(isinstance(mygame[1][0], Wall))
        self.assertTrue(isinstance(mygame[1][1], Robot))
        self.assertTrue(isinstance(mygame[1][2], Exit))
        self.assertTrue(isinstance(mygame[2][0], Wall))
        self.assertTrue(isinstance(mygame[2][1], Wall))
        self.assertTrue(isinstance(mygame[2][2], Wall))
