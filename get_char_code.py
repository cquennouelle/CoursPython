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
            if char_ == '\x1b':
                # Read an arrow or other special character
                char_ += sys.stdin.read(2)
            else:
                char_ = char_.upper()
                if char_ == 'E' or char_ == 'S' or char_ == 'W' or char_ == 'N':
                    # Read a multiple movement
                    next_char = sys.stdin.read(1)
                    if next_char in \
                        ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        char_ += next_char
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
        command = 'up'
    elif k == '\x1b[B':
        command = 'down'
    elif k == '\x1b[C':
        command = 'right'
    elif k == '\x1b[D':
        command = 'left'
    elif k == 'q' or k == 'Q':
        command = 'end'
    elif k[0] == 'E' or k[0] == 'S' or k[0] == 'W' or k[0] == 'N':
        if len(k) > 1:
            print('multiple: {}'.format(k))
        else:
            k += '1'
        command = k
    else:
        print('not an arrow key! ({})'.format(k))
        command = ''
    return command

def main():
    """Main method of the module."""
    for _ in range(0, 25):
        get()

if __name__ == '__main__':
    main()
