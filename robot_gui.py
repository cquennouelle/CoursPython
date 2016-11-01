# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 09:52:33 2016

@author: localuser
"""

import roboc
import Tkinter

class RobocGUI(Tkinter.Frame):
    """Class to play in a TKinter window."""

    def __init__(self, wind, **kwargs):
        """Construction."""
        Tkinter.Frame.__init__(self,
                               wind,
                               width=768,
                               height=576,
                               **kwargs)
        self.pack(fill=Tkinter.BOTH)
        self.nb_clicks = 0

        self.message = Tkinter.Label(self,
                                     text='You haven\'t click on the button.')
        self.message.pack()
        self.quit_button = Tkinter.Button(self,
                                          text='Exit',
                                          command=self.quit)
        self.quit_button.pack(side='left')
        self.click_button = Tkinter.Button(self,
                                           text='Click here',
                                           fg='red',
                                           command=self.on_click)
        self.click_button.pack(side='right')
        self.roboc = roboc.Roboc('maps')

    def on_click(self):
        """Action when buttonis clicked."""
        self.nb_clicks += 1
        self.message['text'] = 'You clicked {} times'.format(self.nb_clicks)

if __name__ == '__main__':
    WIND = Tkinter.Tk()
    ROBOC_GUI = RobocGUI(WIND)
    ROBOC_GUI.mainloop()
    WIND.destroy()
