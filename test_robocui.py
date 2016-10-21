# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:18:12 2016

@author: localuser
"""

import unittest
from robocui import RobocUI

class RobocUITest(unittest.TestCase):
    """Test class roboc_interface."""

    def test_init(self):
        """Test construction Roboc interface."""
        RobocUI('testmazedicttwo')
        self.assertTrue(True)

#    def test_run(self):
#        """Test run."""
#        rob = RobocInterface('testmazedicttwo')
#        rob.run()
#        self.assertTrue(True)
        