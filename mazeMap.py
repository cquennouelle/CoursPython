# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 20:15:18 2016

@author: localuser
"""

class MazeMap:
    """Class representing a map."""
    
    def LoadFromString(self, string):
        size = len(string)
        self.height = 0
        self.width = 0
        self.grid = []
        if size > 0:
            rows = string.split(sep='\n')
            self.height = 0
            for row in rows:
                gridRow = []
                for letter in row:
                    gridRow.append(letter)
                self.grid.append(gridRow)
            self.height = len(self.grid)
            self.width = len(rows)
    
    def __init__(self, string=''):
        if type(string) is not str:
            raise TypeError("Requires a string to build a maze.")
        if string == '':
            self.height = 0
            self.width = 0
            self.grid = []
        else:
            self.LoadFromString(string)
    
    def __repr__(self):
        return "<Map {}x{}>".format(self.height, self.width)
        
    def getAsString(self):
        string = str('')
        for row in self.grid:
            for col in row:
                string += col
            string += '\n'
        return string[0:len(string)-1]
    