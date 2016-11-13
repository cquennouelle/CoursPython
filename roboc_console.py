# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 21:24:19 2016

@author: localuser
"""

from __future__ import print_function
import roboc_ui
import os
if os.name == 'posix':
    import get_char_code
import roboc_command

class RobocConsole(roboc_ui.RobocUI):
    """Class to interact through console."""

    def __init__(self):
        """Construction."""
        super(RobocConsole, self).__init__()

    @staticmethod
    def _clear_screen():
        """Clear screen depending on os."""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def _get_code_command_linux():
        """Get command from keyboard."""
        print('Use arrows (or \'E\', \'S\', \'W\',' +\
            '\'N\' + a number) to move  or \'q\' to give up.')
        return get_char_code.get()

    @staticmethod
    def _get_code_command_windows():
        """Get command from keyboard."""
        while 1:
            print('Use \'E\', \'S\', \'W\', \'N\'' +\
                '[+ 1-9] to move. Or \'q\' to give up.')
            hitkeys = input()
            if len(hitkeys) > 0:
                char_ = hitkeys[0].upper()
                if char_ in 'ESNW':
                    if len(hitkeys) == 2:
                        num_ = hitkeys[1]
                        if num_ in '123456789':
                            return char_ + num_
                    else:
                        return char_ + '1'
                elif char_ == 'Q':
                    return 'end'

    def _build_command(self, code_command):
        """Build command from string."""
        if code_command == 'end':
            return roboc_command.RobocCommandExit()
        elif code_command[0] == 'E':
            return roboc_command.RobocMoveEast(int(code_command[1:]))
        elif code_command[0] == 'W':
            return roboc_command.RobocMoveWest(int(code_command[1:]))
        elif code_command[0] == 'S':
            return roboc_command.RobocMoveSouth(int(code_command[1:]))
        elif code_command[0] == 'N':
            return roboc_command.RobocMoveNorth(int(code_command[1:]))
        else:
            print(code_command)
            raise ValueError()

    def get_command(self):
        """Get the command depending on os."""
        if os.name == 'posix':
            code_command = self._get_code_command_linux()
        elif  os.name == 'nt':
            code_command = self._get_code_command_windows()
        command = self._build_command(code_command)
        return command

    def update_display(self):
        """Display stuff at the beginning of each turn."""
        self._clear_screen()
        print('Your score is {}'.format(self._roboc.score))
        print(self._roboc.currentmaze)
        print("Your viewpoint:")
        print(self._roboc.get_hidden_game(4))

    def print_message(self, message):
        """Print message to screen."""
        print(message)

if __name__ == '__main__':
    RI = RobocConsole()
    RI.run()
