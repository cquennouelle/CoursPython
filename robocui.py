# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:21:53 2016

@author: localuser
"""

from __future__ import print_function
from roboc import Roboc
import get_char_code

class RobocUI(object):
    """Class managing interaction with roboc."""

    def __init__(self, directory):
        """Construction."""
        self._roboc = Roboc(directory)

    def _print_mazelist(self):
        """Print list of available mazes to choose."""
        print('0 - autosave')
        mazedict = self._roboc.mazedict
        for n_maze in range(mazedict.size):
            print(str(n_maze+1) + " - " + mazedict.get_name(n_maze))

    def _select_maze(self):
        """Method to manage maze selection."""
        nmaze = input('Enter selected maze number (1-{}): '.format(
            self._roboc.mazedict.size))
        try:
            nmaze = int(nmaze)
            if nmaze < 0 or nmaze > self._roboc.mazedict.size:
                    print("Please, enter a number between 0 and {}.".format(
                        self._roboc.mazedict.size))
                    self._select_maze()
            else:
                if(nmaze == 0):
                    self._roboc.reloadautosave()
                    print('Reload last game')
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
        while hitkey != 'end' and not self._roboc.is_won():
            print(self._roboc.game)
            print('Use arrows or \'x\' to give up.')
            hitkey = get_char_code.get()
            if hitkey == 'down':
                self._roboc.move_south(1)
            elif hitkey == 'up':
                self._roboc.move_north(1)
            elif hitkey == 'left':
                self._roboc.move_west(1)
            elif hitkey == 'right':
                self._roboc.move_east(1)
            elif hitkey[0] == 'E':
                self._roboc.move_east(int(hitkey[1]))
            elif hitkey[0] == 'S':
                self._roboc.move_south(int(hitkey[1]))
            elif hitkey[0] == 'N':
                self._roboc.move_north(int(hitkey[1]))
            elif hitkey[0] == 'W':
                self._roboc.move_west(int(hitkey[1]))
        if(self._roboc.is_won()):
            print('You\'re out. Congratulations.')
        else:
            print('Looser...')

    def run(self):
        """Test run roboc."""
        self._print_mazelist()
        self._select_maze()
        self._play_game()

if __name__ == '__main__':
    RI = RobocUI('testmazedicttwo')
    RI.run()
    