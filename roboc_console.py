# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 21:24:19 2016

@author: localuser
"""

import roboc_interactions

class RobocConsole(object):
    """Class to interact through console."""

    def __init__(self):
        """Construction."""
        self.robocui = roboc_interactions.RobocInteractions('maps')

    def run(self):
        """Test run roboc."""
        self.robocui.launch_game()
        self.robocui.play_game()

if __name__ == '__main__':
    RI = RobocConsole()
    RI.run()
