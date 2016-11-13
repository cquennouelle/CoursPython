# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 09:52:33 2016

@author: localuser
"""

import roboc_ui
import tkinter
import roboc_window

class RobocGUI(roboc_ui.RobocUI):
    """Class to play in a TKinter window."""

    def __init__(self, wind):
        """Construction."""
        super(RobocGUI, self).__init__()
        self.window = roboc_window.RobocWindow(wind)
        print('Launch mainloop')
        #self.window.mainloop()

    def get_command(self):
        """Get the command."""
        command = input('Your command: ')
        return command

    def update_display(self):
        """Display stuff at the beginning of each turn."""
        string_to_display = str(self._roboc.score)+\
            str(self._roboc.currentmaze)+'\n\n'+\
            'Your viewpoint:'+'\n'+\
            self._roboc.get_hidden_game(4)
        print(string_to_display)
        self.window.update_message(string_to_display)
        
    def print_message(self, message):
        """Method to print."""
        self.window.update_message(message)

if __name__ == '__main__':
    WIND = tkinter.Tk()
    RI = RobocGUI(WIND)
    RI.run()
    WIND.destroy()
