import json

__author__ = 'ko3a4ok'
import os, math
from base64 import b64encode
class Game:
    n = 32
    def __init__(self, name):
        self.name = name;
        self.id = str(b64encode(os.urandom(int(math.ceil(0.75*Game.n))),'-_')[:Game.n])
        self.status = 'free'
        self.player1 = None
        self.player2 = None


    def getJsonFormatted(self):
        result = {'id' : self.id, 'name' : self.name, 'status' : self.status}
        if self.player1 != None:
            result['players']=[self.player1.name]
        if self.player2 != None:
            result['players'].append(self.player2.name)
        return result

    def connectUser(self, user):
        if self.player1 == None:
            self.player1 = user;
            self.status='open'
        elif self.player2 == None and self.player1 != user:
            self.player2 = user;
            self.status='full'
            self.player1.notifications.append({'action': 'startGame', 'data':{'color': 'white'}})
            self.player2.notifications.append({'action': 'startGame', 'data':{'color': 'black'}})
        else :
            raise Exception('Fuck')

    def movement(self, fromPos, toPos):
        n = {'action': 'movement', 'data':{'from': fromPos, 'to' : toPos}}
        self.player1.notifications.append(n)
        self.player2.notifications.append(n)



