# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 09:42:38 2016

@author: localuser
"""

import roboc_interactions

class IRobocUI(object):
    """Interface for UI classes."""

    def __init__(self):
        """Construction."""
        self.robocui = roboc_interactions.RobocInteractions(
            directory='maps',
            robocui=self)

    def _set_roboc(self, roboc):
        """Bind to an instance of roboc."""
        self._roboc = roboc

    def run(self):
        """Test run roboc."""
        self.robocui.launch_game()
        self.robocui.play_game()

    def get_command(self):
        """Get the command depending on os."""
        raise NotImplementedError('Interface for UI')

    def update_display(self):
        """Display stuff at the beginning of each turn."""
        raise NotImplementedError('Interface for UI')
        
    def print(self, message):
        """Method to print."""
        raise NotImplementedError('Interface for UI')

    roboc = property(fset=_set_roboc)
