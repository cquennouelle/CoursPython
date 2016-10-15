# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:20:45 2016

@author: localuser
"""

import unittest
from roboc import *

class RobocTest(unittest.TestCase):
    """Test class Roboc."""

    def test_init(self):
        """Test default construction."""
        rob = Roboc()
