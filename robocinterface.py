# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:21:53 2016

@author: localuser
"""

from __future__ import print_function
from roboc import Roboc
import get_char_code

class RobocInterface(object):
    """Class managing interaction with roboc."""

    def __init__(self, directory):
        """Construction."""
        self._roboc = Roboc(directory)

    def _print_mazelist(self):
        """Print list of available mazes to choose."""
        mazedict = self._roboc.mazedict
        for n_maze in range(mazedict.size):
            print(str(n_maze+1) + " - " + mazedict.get_name(n_maze))

    def _select_maze(self):
        """Method to manage maze selection."""
        nmaze = input('Enter selected maze number (1-{}):'.format(
            self._roboc.mazedict.size))
        try:
            nmaze = int(nmaze)
            if nmaze < 1 or nmaze > self._roboc.mazedict.size:
                print("Please, enter a number between 1 and {}.".format(
                    self._roboc.mazedict.size))
                self._select_maze()
            else:
                self._roboc.select_maze(nmaze-1)
                print('You\'ve selected: {}'.format(
                    self._roboc.mazedict.get_name(nmaze-1)))
        except ValueError:
            print("Please, enter a valid number.")
            self._select_maze()

    def _play_game(self):
        """Method to play."""
        hitkey = ''
        while hitkey != 'end':
            print(self._roboc.game)
            hitkey = get_char_code.get()
            if hitkey == 'down':
                self._roboc.move_south(1)
            elif hitkey == 'up':
                self._roboc.move_north(1)
            elif hitkey == 'left':
                self._roboc.move_west(1)
            elif hitkey == 'right':
                self._roboc.move_east(1)

    def run(self):
        """Test run roboc."""
        self._print_mazelist()
        self._select_maze()
        self._play_game()
