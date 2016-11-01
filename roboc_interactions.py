# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:21:53 2016

@author: localuser
"""

import roboc
#import roboc_console
#import os
#if os.name == 'posix':
#    import get_char_code

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
        self._robocui.print(self._get_mazelist())

    def _input_nmaze(self, mazedictsize):
        """Get number of selected maze."""
        nmaze = input('Enter your choice: '.format(
            mazedictsize))
        try:
            nmaze = int(nmaze)
            if nmaze < 0 or nmaze > mazedictsize:
                self._robocui.print('Please, enter a number between 0 and {}.'.format(mazedictsize))
                return self._input_nmaze(mazedictsize)
            else:
                return nmaze
        except ValueError:
            self._robocui.print("Please, enter a valid number.")
            return self._input_nmaze(mazedictsize)

    def _select_maze(self, nmaze):
        """Method to manage maze selection."""
        if nmaze == 0:
            self._roboc.reloadautosave()
            self._robocui.print('Reload last game')
        else:
            self._roboc.select_maze(nmaze-1)
            self._robocui.print('You\'ve selected: {}'.format(
                self._roboc.mazedict.get_name(nmaze-1)))

#    def _clear_screen(self):
#        """Clear screen depending on os."""
#        if os.name == 'nt':
#            os.system('cls')
#        else:
#            os.system('clear')
#
#    def _get_command_linux(self):
#        """Get command from keyboard."""
#        print('Use arrows (or \'E\', \'S\', \'W\',' +\
#            '\'N\' + a number) to move  or \'q\' to give up.')
#        return get_char_code.get()
#
#    def _get_command_windows(self):
#        """Get command from keyboard."""
#        while 1:
#            print('Use \'E\', \'S\', \'W\', \'N\'' +\
#                '[+ 1-9] to move. Or \'q\' to give up.')
#            hitkeys = input()
#            if len(hitkeys) > 0:
#                char_ = hitkeys[0].upper()
#                if char_ in 'ESNW':
#                    if len(hitkeys) == 2:
#                        num_ = hitkeys[1]
#                        if num_ in '123456789':
#                            return char_ + num_
#                    else:
#                        return char_ + '1'
#                elif char_ == 'Q':
#                    return 'end'
#
#    def _get_command(self):
#        """Get the command depending on os."""
#        if os.name == 'posix':
#            return self._get_command_linux()
#        elif  os.name == 'nt':
#            return self._get_command_windows()

    def launch_game(self):
        """Method to launche game."""
        mazedictsize = self._roboc.mazedict.size
        self._print_mazelist()
        nmaze = self._input_nmaze(mazedictsize)
        self._select_maze(nmaze)
        self._roboc.random_robot_place()
#
#    def _update_display(self):
#        """Display stuff at the beginning of each turn."""
#        self._clear_screen()
#        print('Your score is {}'.format(self._roboc.score))
#        print(self._roboc.currentmaze)
#        print("Your viewpoint:")
#        print(self._roboc.get_hidden_game(4))

    def play_game(self):
        """Method to play."""
        command = ''
        while command != 'end' and not self._roboc.is_won():
            self._robocui.update_display()
            command = self._robocui.get_command()
            if command == 'down':
                self._roboc.move_south(1)
            elif command == 'up':
                self._roboc.move_north(1)
            elif command == 'left':
                self._roboc.move_west(1)
            elif command == 'right':
                self._roboc.move_east(1)
            elif command[0] == 'E':
                self._roboc.move_east(int(command[1]))
            elif command[0] == 'S':
                self._roboc.move_south(int(command[1]))
            elif command[0] == 'N':
                self._roboc.move_north(int(command[1]))
            elif command[0] == 'W':
                self._roboc.move_west(int(command[1]))
            elif command == 'end':
                return
            else:
                self._robocui.print('Not a correct command.')
        if self._roboc.is_won():
            self._robocui.print('You\'re out. Congratulations.')
            self._robocui.print(self._roboc.game)
        else:
            self._robocui.print('Looser...')
