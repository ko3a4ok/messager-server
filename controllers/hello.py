from array import array
import logging

from helloworld.lib.base import *
from pylons import request, g, session
from pylons.templating import render
from time import time
import uuid
log = logging.getLogger(__name__)

class HelloController(BaseController):

    def index(self):
            # Return a rendered template
            #   return render('/some/template.mako')
            # or, Return a response
            return 'Hello World'
    def serverinfo(self):
        import cgi
        import pprint
        c.pretty_environ = cgi.escape(pprint.pformat(request.environ))
        c.name = 'The Black Knight'
        return render('/serverinfo.mako')


    def __initConnection(self):
        key = str(uuid.uuid4())
        session['user_id'] = str(key);
        session.save();
        g.map[key] = []

    def getNotification(self):
        if not session.get('user_id'):
            self.__initConnection();
        if not g.map.get(session['user_id']):
            self.__initConnection();
        ls = g.map[session['user_id']]
        start = time();
        while len(ls) == 0 :
            if (time()-start > 30):
                return '';
            pass
        response = str(ls.pop())
        return response

    def app_globals_test(self):
        g.n += 1
        if g.message != 'Hello':
            content = 'Hello ' + ' ' + str(g.n)
            g.message = content
            lines = request.body.readlines()
            content += "this is content = |%s|\n" % str(lines)
#            g.queue.append(lines[0])
            for key in g.map.keys() :
                ls = g.map[key]
                ls.append(lines[0])
            content += "header  = %s\n" % request.headers['head1']
            if session.get('user_id') :
                content += "session user_id %s" % session.get('user_id');
            return content
        else:
            return g.message