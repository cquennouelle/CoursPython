# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 13:55:27 2016

@author: localuser
"""
import unittest
import roboc
import roboc_command
#from mock import Mock
#from mock import MagicMock  # import MagicMock

class RobocMock(roboc.Roboc):
    """Mock."""
    def __init__(self):
        self.calls = {'east':0, 'south':0, 'west':0, 'north':0}
    def move_east(self, nb_times):
        self.calls['east'] += nb_times
    def move_south(self, nb_times):
        self.calls['south'] += nb_times
    def move_west(self, nb_times):
        self.calls['west'] += nb_times
    def move_north(self, nb_times):
        self.calls['north'] += nb_times

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

        n = roboc_command.RobocCommandExit()
        self.assertTrue(isinstance(n, roboc_command.RobocCommand))
        self.assertTrue(isinstance(n, roboc_command.RobocCommandExit))

    def test_execute_east(self):
        """Test method execute."""
        mock = RobocMock()
        com = roboc_command.RobocMoveEast()
        com.execute(mock)
        self.assertEqual(mock.calls['east'], 1)
        self.assertEqual(mock.calls['south'], 0)
        self.assertEqual(mock.calls['west'], 0)
        self.assertEqual(mock.calls['north'], 0)
        com2 = roboc_command.RobocMoveEast(10)
        com2.execute(mock)
        self.assertEqual(mock.calls['east'], 11)
        self.assertEqual(mock.calls['south'], 0)
        self.assertEqual(mock.calls['west'], 0)
        self.assertEqual(mock.calls['north'], 0)

    def test_execute_west(self):
        """Test method execute."""
        mock = RobocMock()
        com = roboc_command.RobocMoveWest()
        com.execute(mock)
        self.assertEqual(mock.calls['east'], 0)
        self.assertEqual(mock.calls['south'], 0)
        self.assertEqual(mock.calls['west'], 1)
        self.assertEqual(mock.calls['north'], 0)
        com2 = roboc_command.RobocMoveWest(10)
        com2.execute(mock)
        self.assertEqual(mock.calls['east'], 0)
        self.assertEqual(mock.calls['south'], 0)
        self.assertEqual(mock.calls['west'], 11)
        self.assertEqual(mock.calls['north'], 0)

    def test_execute_south(self):
        """Test method execute."""
        mock = RobocMock()
        com = roboc_command.RobocMoveSouth()
        com.execute(mock)
        self.assertEqual(mock.calls['east'], 0)
        self.assertEqual(mock.calls['south'], 1)
        self.assertEqual(mock.calls['west'], 0)
        self.assertEqual(mock.calls['north'], 0)
        com2 = roboc_command.RobocMoveSouth(10)
        com2.execute(mock)
        self.assertEqual(mock.calls['east'], 0)
        self.assertEqual(mock.calls['south'], 11)
        self.assertEqual(mock.calls['west'], 0)
        self.assertEqual(mock.calls['north'], 0)

    def test_execute_north(self):
        """Test method execute."""
        mock = RobocMock()
        com = roboc_command.RobocMoveNorth()
        com.execute(mock)
        self.assertEqual(mock.calls['east'], 0)
        self.assertEqual(mock.calls['south'], 0)
        self.assertEqual(mock.calls['west'], 0)
        self.assertEqual(mock.calls['north'], 1)
        com2 = roboc_command.RobocMoveNorth(10)
        com2.execute(mock)
        self.assertEqual(mock.calls['east'], 0)
        self.assertEqual(mock.calls['south'], 0)
        self.assertEqual(mock.calls['west'], 0)
        self.assertEqual(mock.calls['north'], 11)
        