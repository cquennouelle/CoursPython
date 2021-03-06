# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:21:53 2016

@author: localuser
"""

import roboc
import roboc_command

class RobocInteractions(object):
    """Class managing interaction with roboc."""

    def __init__(self, directory, robocui):
        """Construction."""
        self._roboc = roboc.Roboc(directory)
        self._robocui = robocui
        self._robocui.roboc = self._roboc

    def _get_mazelist(self):
        """Build list of available mazes to choose."""
        str_list = '0 - autosave\n'
        mazedict = self._roboc.mazedict
        for n_maze in range(mazedict.size):
            str_list += str(n_maze+1) + " - " + mazedict.get_name(n_maze) + '\n'
        return str_list

    def _print_mazelist(self):
        """Print list of available mazes to choose."""
        self._robocui.print_message(self._get_mazelist())

    def _input_nmaze(self, mazedictsize):
        """Get number of selected maze."""
        nmaze = input('Enter your choice: '.format(
            mazedictsize))
        try:
            nmaze = int(nmaze)
            if nmaze < 0 or nmaze > mazedictsize:
                self._robocui.print_message('Please, enter a number between 0 and {}.'.format(mazedictsize))
                return self._input_nmaze(mazedictsize)
            else:
                return nmaze
        except ValueError:
            self._robocui.print_message("Please, enter a valid number.")
            return self._input_nmaze(mazedictsize)

    def _select_maze(self, nmaze):
        """Method to manage maze selection."""
        if nmaze == 0:
            self._roboc.reloadautosave()
            self._robocui.print_message('Reload last game')
        else:
            self._roboc.select_maze(nmaze-1)
            self._robocui.print_message('You\'ve selected: {}'.format(
                self._roboc.mazedict.get_name(nmaze-1)))

    def launch_game(self):
        """Method to launche game."""
        mazedictsize = self._roboc.mazedict.size
        self._print_mazelist()
        nmaze = self._input_nmaze(mazedictsize)
        self._select_maze(nmaze)
        self._roboc.random_robot_place()

    def play_game(self):
        """Method to play."""
        command = ''
        while not self._roboc.is_won():
            self._robocui.update_display()
            command = self._robocui.get_command()
            command.execute(self._roboc)
            if isinstance(command, roboc_command.RobocCommandExit):
                break
        if self._roboc.is_won():
            self._robocui.print_message('You\'re out. Congratulations.')
            self._robocui.print_message(self._roboc.game)
        else:
            self._robocui.print_message('Looser...')
