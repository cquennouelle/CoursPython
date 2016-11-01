# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:18:12 2016

@author: localuser
"""

import unittest
from roboc_interactions import RobocInteractions

class RobocInteractionsTest(unittest.TestCase):
    """Test class roboc_interactions."""

    def test_init(self):
        """Test construction Roboc interface."""
        RobocInteractions('testmazedicttwo')
        self.assertTrue(True)

#    def test_run(self):
#        """Test run."""
#        rob = RobocInterface('testmazedicttwo')
#        rob.run()
#        self.assertTrue(True)
        