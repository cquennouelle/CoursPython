# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:17:58 2016

@author: cquennouelle
"""

import mazedict

class Roboc(object):
    """Class containing the game Roboc."""

    def __init__(self, directory='mazemaps'):
        """Construction."""
        self._mazedict = mazedict.Mazedict()
        self._mazedict.autosearch(directory)
        self._currentmaze = self._mazedict['mini']
        self._robot_place = (1, 1)

    def _get_mazedict(self):
        """Get mazedict."""
        return self._mazedict

    def _get_currentmaze(self):
        """Get the selected maze."""
        return self._currentmaze

    def select_maze(self, maze='mini'):
        """Select a maze by its name."""
        if type(maze) is str:
            self._currentmaze = self._mazedict[maze]
        elif type(maze) is int:
            self._currentmaze = self._mazedict[maze]
        else:
            raise TypeError

    def _move_south(self):
        """Move robot of 1 cell south."""
        content = self._currentmaze[self._robot_place[0]+1, \
            self._robot_place[1]]
        if content.is_crossable():
            self._robot_place = (self._robot_place[0] + 1, self._robot_place[1])

    def move_south(self, nb_cells):
        """Move robot of nb_cells south."""
        for _ in range(nb_cells):
            self._move_south()

    def _move_east(self):
        """Move robot of 1 cell east."""
        content = self._currentmaze[self._robot_place[0], \
            self._robot_place[1]+1]
        if content.is_crossable():
            self._robot_place = (self._robot_place[0], self._robot_place[1]+1)

    def move_east(self, nb_cells):
        """Move robot of nb_cells east."""
        for _ in range(nb_cells):
            self._move_east()

    def _move_west(self):
        """Move robot of 1 cell west."""
        content = self._currentmaze[self._robot_place[0], \
            self._robot_place[1]-1]
        if content.is_crossable():
            self._robot_place = (self._robot_place[0], self._robot_place[1]-1)

    def move_north(self, nb_cells):
        """Move robot of nb_cells north."""
        for _ in range(nb_cells):
            self._move_north()

    def _move_north(self):
        """Move robot of 1 cell north."""
        content = self._currentmaze[self._robot_place[0]-1, \
            self._robot_place[1]]
        if content.is_crossable():
            self._robot_place = (self._robot_place[0]-1, self._robot_place[1])

    def move_west(self, nb_cells):
        """Move robot of nb_cells west."""
        for _ in range(nb_cells):
            self._move_west()

    def _get_robot_place(self):
        """Get robot place."""
        return self._robot_place

    def _get_game(self):
        """Method to get the game board."""
        occupiedgrid = self._currentmaze.get_game(self.robot_place)
        string = str('')
        for row in occupiedgrid:
            for col in row:
                string += str(col)
            string += '\n'
        return string[0:len(string)-1]
    
    def is_won():
        """Method to know if the game is won."""
        return false

    currentmaze = property(_get_currentmaze)
    robot_place = property(_get_robot_place)
    mazedict = property(_get_mazedict)
    game = property(_get_game)
