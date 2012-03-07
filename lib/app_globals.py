"""The application's Globals object"""
from array import array
from pylons import config

class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application
    """

    def __init__(self):
        """One instance of Globals is created during application
        initialization and is available during requests via the 'g'
        variable
        """
        self.map = {}
        self.message = 'Hello dron'
        self.n = 0
        self.queue = []
        pass
