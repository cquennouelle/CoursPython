# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:29:14 2016

@author: cquennouelle
"""

import unittest
from mazemap import *

class MazemapTest(unittest.TestCase):
    """Test class MazeMap."""
    
    def test_init_with_parameters_error(self):
        """Test construction error when wrong parameter type."""
        with self.assertRaises(TypeError):
            mymap = Mazemap(1)

    def test_init_1(self):
        """Test for empty construction."""
        mymap = Mazemap()
        self.assertEqual(mymap._grid, [])

    def test_init_2(self):
        """Test construction from an empty string."""
        mymap = Mazemap('')
        self.assertEqual(mymap._grid, [])
            
    def test_init_3(self):
        """Test construction from a string."""
        mymap = Mazemap('OOO\nO U\nOOO')
        self.assertEqual(mymap._grid, 
                         [['O', 'O', 'O'], ['O', ' ', 'U'], ['O', 'O', 'O']])
        
    def test_get_as_string(self):
        """Test method get_as_string."""
        string = 'OOO\nO U\nOOO'
        mymap = Mazemap(string)
        self.assertEqual(mymap.get_as_string(), string)
        
    def test_init_from_file(self):
        """Test construction from a file."""
        mymap = Mazemap(filename="LoadMazeFromFile.test")
        self.assertEqual(mymap._grid, 
                         [['O', 'O', 'O'], ['O', ' ', 'U'], ['O', 'O', 'O']])
        
    def test_save_file(self):  
        """Test saving mazemap in a file."""
        mymap = Mazemap('OOO\nO U\nOOO')
        mymap.save_to_file('SaveMaze.test')
        mymap2 = Mazemap(filename="SaveMaze.test")
        self.assertEqual(mymap2._grid, 
                         [['O', 'O', 'O'], ['O', ' ', 'U'], ['O', 'O', 'O']])
         
