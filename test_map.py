# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:29:14 2016

@author: cquennouelle
"""

import unittest
from mazeMap import *

class MapTest(unittest.TestCase):
    """Test class Map."""
    
    def testInitWithParametersError(self):
        """Test construction error when wrong parameter type."""
        with self.assertRaises(TypeError):
            myMap = MazeMap(1)

    def testInit(self):
        """Test for empty construction."""
        myMap = MazeMap()
        self.assertEqual(myMap.height, 0)
        self.assertEqual(myMap.width, 0)
        self.assertEqual(myMap.grid, [])

    def testInit2(self):
        """Test construction from an empty string."""
        myMap = MazeMap('')
        self.assertEqual(myMap.height, 0)
        self.assertEqual(myMap.width, 0)
        self.assertEqual(myMap.grid, [])
            
    def testInit3(self):
        """Test construction from a string."""
        myMap = MazeMap('OOO\nO U\nOOO')
        self.assertEqual(myMap.height, 3)
        self.assertEqual(myMap.width, 3)
        self.assertEqual(myMap.grid, [['O', 'O', 'O'], ['O', ' ', 'U'], ['O', 'O', 'O']])
        
    def testGetAsString(self):
        string = 'OOO\nO U\nOOO'
        myMap = MazeMap(string)
        self.assertEqual(myMap.getAsString(), string)
        
    def testLoadFromFile(self):
        myMap = MazeMap(fileName = "LoadMazeFromFile.test")
        self.assertEqual(myMap.grid, [['O', 'O', 'O'], ['O', ' ', 'U'], ['O', 'O', 'O']])
        
    def testSaveFile(self):        
        myMap = MazeMap('OOO\nO U\nOOO')
        myMap.saveToFile('SaveMaze.test')
        myMap2 = MazeMap(fileName = "SaveMaze.test")
        self.assertEqual(myMap2.grid, [['O', 'O', 'O'], ['O', ' ', 'U'], ['O', 'O', 'O']])
        
        
         
