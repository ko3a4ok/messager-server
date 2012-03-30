"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('error/:action/:id', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('/move', controller='chess', action='move')
    map.connect('/getNotifications', controller='chess', action='getNotifications')
    map.connect('/connectToGame', controller='chess', action='connectToGame')
    map.connect('/initClient', controller='chess', action='initClient')
    map.connect('/getUser', controller='chess', action='getUser')
    map.connect('/addUser', controller='chess', action='addUser')
    map.connect('/getGamesList', controller='chess', action='getGamesList')
    map.connect('/n', controller='hello', action='getNotification')
    map.connect('/i', controller='hello', action='serverinfo')
    map.connect('/f', controller='hello', action='app_globals_test')
    map.connect('/', controller='hello', action='index')
    map.connect(':controller/:action/:id')
    map.connect('*url', controller='template', action='view')

    return map
