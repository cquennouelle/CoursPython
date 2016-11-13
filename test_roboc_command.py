# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 13:55:27 2016

@author: localuser
"""
import unittest
import roboc_command

class RobocCommandTest(unittest.TestCase):
    """Tests for RobocCommand."""
    
    def test_init(self):
        """Test construction."""
        e = roboc_command.RobocMoveEast()
        self.assertTrue(isinstance(e, roboc_command.RobocCommand))
        self.assertTrue(isinstance(e, roboc_command.RobocCommandMove))
        self.assertTrue(isinstance(e, roboc_command.RobocMoveEast))
        self.assertEqual(e.nb_times, 1)
        e2 = roboc_command.RobocMoveEast(2)
        self.assertEqual(e2.nb_times, 2)
        
        w = roboc_command.RobocMoveWest()
        self.assertTrue(isinstance(w, roboc_command.RobocCommand))
        self.assertTrue(isinstance(w, roboc_command.RobocCommandMove))
        self.assertTrue(isinstance(w, roboc_command.RobocMoveWest))
        self.assertEqual(w.nb_times, 1)
        w2 = roboc_command.RobocMoveWest(2)
        self.assertEqual(w2.nb_times, 2)
        
        s = roboc_command.RobocMoveSouth()
        self.assertTrue(isinstance(s, roboc_command.RobocCommand))
        self.assertTrue(isinstance(s, roboc_command.RobocCommandMove))
        self.assertTrue(isinstance(s, roboc_command.RobocMoveSouth))
        self.assertEqual(s.nb_times, 1)
        s2 = roboc_command.RobocMoveSouth(2)
        self.assertEqual(s2.nb_times, 2)
        
        n = roboc_command.RobocMoveNorth()
        self.assertTrue(isinstance(n, roboc_command.RobocCommand))
        self.assertTrue(isinstance(n, roboc_command.RobocCommandMove))
        self.assertTrue(isinstance(n, roboc_command.RobocMoveNorth))
        self.assertEqual(n.nb_times, 1)
        n2 = roboc_command.RobocMoveNorth(2)
        self.assertEqual(n2.nb_times, 2)
        
        