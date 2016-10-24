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
            char_ = sys.stdin.read(1)
            if char_== '\x1b':
                # Read an arrow or other special character
                char_ += sys.stdin.read(2)
            else:
                char_ = char_.upper()
                if char_ == 'E' or char_ == 'S' or char_ == 'W' or char_ == 'N':
                    # Read a multiple movement
                    char_ += sys.stdin.read(1)
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
    elif k == 'q' or k == 'Q':
        return 'end'
    elif k[0] == 'E' or k[0] == 'S' or k[0] == 'W' or k[0] == 'N':
        print('multiple: {}'.format(k))
        return k        
    else:
        print('not an arrow key! ({})'.format(k))
        return ''

def main():
    """Main method of the module."""
    for _ in range(0, 25):
        get()

if __name__ == '__main__':
    main()
