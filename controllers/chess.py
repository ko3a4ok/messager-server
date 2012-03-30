import json
from helloworld.lib.base import BaseController
from helloworld.model.user import User
from helloworld.model.game import Game
from time import time
import uuid
from pylons import session, request, g



__author__ = 'ko3a4ok'
class ChessController(BaseController):

    users = {}
    def __init__(self):
        super(ChessController, self).__init__()

    games = {}
    def initGames(self):
        gameName = ['Zhytomyr', 'kaZantip', 'Las Vegas', 'Ibizza']
        for name in gameName :
            game = Game(name);
            self.games[game.id] = game;



    def __initConnection(self):
        key = str(uuid.uuid4())
        session['user_id'] = str(key);
        session.save();

    def addUser(self):
        if 'name' not in request.params:
            return 'false';
        self.__initConnection();
        key = session['user_id']
        user = User(request.params['name'])
        user.token = key;
        ChessController.users[key] = user;
        return user.getJsonFormatted()

    def __findUser(self, userId):
        for user in ChessController.users.values():
            if user.id == userId:
                return user;
        return None;

    def connectToGame(self):
        user = self.__getUser();
        if user == None:
            return 'Unsigned client';
        if not request.params.has_key('gameId') :
            return 'gameId not exists'
        gameId = request.params['gameId'];
        if not ChessController.games.has_key(gameId):
            return 'game not found';
        game = ChessController.games[gameId]
        try:
            game.connectUser(user)
            user.game = game
            return 'ok';
        except Exception:
            return 'cannot connect to game'


    def initClient(self):
        if 'id' not in request.params:
                return {'error' : 'param id is exist'};
        user = self.__findUser(request.params['id']);
        if (user == None):
            return {'error' : 'user not found'};
        self.__initConnection();
        key = session['user_id']
        if ChessController.users.has_key(user.token) :
            del ChessController.users[user.token]
        user.token =  key
        ChessController.users[key] = user;
        return user.getJsonFormatted()


    def __getUser(self):
        if not session.get('user_id'):
            return None ;
        key = session['user_id']
        if not ChessController.users.has_key(key):
            return None;
        return ChessController.users[key]

    def getUser(self):
        user = self.__getUser();
        if user == None:
            return 'Unsigned user'
        return user.getJsonFormatted();

    def getNotifications(self):
        user = self.__getUser();
        if user == None:
            return 'Unsigned client';
        start = time();
        while len(user.notifications) == 0 :
            if (time()-start > 60):
                return '[]';
            pass
        response = str(user.notifications)
        del user.notifications[:]
        return response


    def move(self):
        user = self.__getUser();
        if user == None:
            return 'Unsigned client';
        if user.game == None:
            return 'User is not player';
        fromPos = request.params['from']
        toPos = request.params['to']
        user.game.movement(fromPos, toPos)


    def getGamesList(self):
        if (len(self.games) == 0) :
            self.initGames()
        result = []
        for game  in self.games.values():
            result.append(game.getJsonFormatted());
        return  result

