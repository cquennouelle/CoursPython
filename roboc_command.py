# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 14:34:39 2016

@author: localuser
"""

class RobocCommand(object):
    """Class for managing commands."""

    def __init__(self):
        """Construction."""
        pass

    def execute(self):
        """Main method."""
        raise NotImplementedError

class RobocCommandMove(RobocCommand):
    """Class for move."""

    def __init__(self, nb_times):
        """Construction."""
        super(RobocCommandMove, self).__init__()
        self._nb_times = nb_times

    def execute(self):
        """Main method."""
        raise NotImplementedError

    def _get_nb_times(self):
        """Accessor for nb_times."""
        return self._nb_times

    nb_times = property(_get_nb_times)

class RobocMoveEast(RobocCommandMove):
    """Move robot East nb_times."""

    def __init__(self, nb_times=1):
        """Construction."""
        super(RobocMoveEast, self).__init__(nb_times)

    def execute(self):
        """Main method."""
        pass

class RobocMoveWest(RobocCommandMove):
    """Move robot West nb_times."""

    def __init__(self, nb_times=1):
        """Construction."""
        super(RobocMoveWest, self).__init__(nb_times)

    def execute(self):
        """Main method."""
        pass

class RobocMoveSouth(RobocCommandMove):
    """Move robot South nb_times."""

    def __init__(self, nb_times=1):
        """Construction."""
        super(RobocMoveSouth, self).__init__(nb_times)

    def execute(self):
        """Main method."""
        pass

class RobocMoveNorth(RobocCommandMove):
    """Move robot North nb_times."""

    def __init__(self, nb_times=1):
        """Construction."""
        super(RobocMoveNorth, self).__init__(nb_times)

    def execute(self):
        """Main method."""
        pass
