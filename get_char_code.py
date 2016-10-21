# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:25:02 2016

@author: localuser
"""
import sys, tty, termios

class _Getch(object):
    """Class used to catch key hits."""
    def __call__(self):
        fd_ = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd_)
        try:
            tty.setraw(sys.stdin.fileno())
            """TODO: manage single character."""
            char_ = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd_, termios.TCSADRAIN, old_settings)
        return char_

def get():
    """Wait for a key to be hit."""
    inkey = _Getch()
    while 1:
        k = inkey()
        if k != '':
            break
    if k == '\x1b[A':
        return 'up'
    elif k == '\x1b[B':
        return 'down'
    elif k == '\x1b[C':
        return 'right'
    elif k == '\x1b[D':
        return 'left'
    elif k == 'xxx':
        return 'end'
    else:
        print('not an arrow key! ({})'.format(k))
        return ''

def main():
    """Main method of the module."""
    for _ in range(0, 25):
        get()

if __name__ == '__main__':
    main()