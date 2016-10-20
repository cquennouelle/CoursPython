# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:18:12 2016

@author: localuser
"""

import unittest
from robocinterface import RobocInterface

class RobocInterfaceTest(unittest.TestCase):
    """Test class roboc_interface."""

    def test_init(self):
        """Test construction Roboc interface."""
        _ = RobocInterface('testmazedicttwo')
        self.assertTrue(True)

#    def test_run(self):
#        """Test run."""
#        rob = RobocInterface('testmazedicttwo')
#        rob.run()
#        self.assertTrue(True)
        