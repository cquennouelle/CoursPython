# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 09:52:33 2016

@author: localuser
"""

import roboc
import tkinter

class RobocWindow(tkinter.Frame):
    """Class to play in a TKinter window."""

    def __init__(self, wind, **kwargs):
        """Construction."""
        tkinter.Frame.__init__(self,
                               wind,
                               width=768,
                               height=576,
                               **kwargs)
        self.pack(fill=tkinter.BOTH)

        self.message = tkinter.Label(self,
                                     text='You haven\'t click on the button.')
        self.message.pack()
        self.maze_list = tkinter.ListBox(self)
#        self.quit_button = tkinter.Button(self,
#                                          text='Exit',
#                                          command=self.quit)
#        self.quit_button.pack(side='left')
#        self.click_button = tkinter.Button(self,
#                                           text='Click here',
#                                           fg='red',
#                                           command=self.on_click)
#        self.click_button.pack(side='right')
#        self.roboc = roboc.Roboc('maps')
        
    def fill_mazelist(self, mazelist):
        """Built listbox to select maze."""
        n = 0
        for maze in mazelist.split('\n')
            self.maze_list.insert(n, maze)
        self.maze_list.pack
        
    def update_message(self, message):
        """Print message in label."""
        self.message['text'] = message
        
#
#    def on_click(self):
#        """Action when buttonis clicked."""
#        self.nb_clicks += 1
#        self.message['text'] = 'You clicked {} times'.format(self.nb_clicks)

if __name__ == '__main__':
    WIND = tkinter.Tk()
    ROBOC_WINDOW = RobocWindow(WIND)
    ROBOC_WINDOW.mainloop()
    WIND.destroy()
