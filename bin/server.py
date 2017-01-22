import cherrypy

class Root(object):
    pass

if __name__ == '__main__':
    cherrypy.tree.mount(Root(), '/', 'app.conf')

    cherrypy.engine.start()
    cherrypy.engine.block()
