from base64 import b64encode
import os
import math

__author__ = 'ko3a4ok'
class User:
    def __init__(self, name):
        self.name = name
        self.rating = 0.0
        self.id = str(b64encode(os.urandom(int(math.ceil(24))),'-_')[:32])
        self.notifications = []
        self.game = None

    def getJsonFormatted(self):
        return {'name' : self.name, 'rating' : self.rating, 'id' : self.id, 'clientId' : self.token}



