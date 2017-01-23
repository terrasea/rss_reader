import cherrypy
from json import JSONEncoder
import requests

import rss_reader

class Root(object):
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def article(self, guid):
        response = requests.get('http://feeds.bbci.co.uk/news/world/rss.xml')

        rss_feed_dict = rss_reader.rss_to_dict(str(response.content, 'utf-8'))

        return rss_reader.get_article(guid, rss_feed_dict)


    @cherrypy.tools.json_out()
    @cherrypy.expose
    def articles(self, keywords=None):
        response = requests.get('http://feeds.bbci.co.uk/news/world/rss.xml')
   
        rss_feed_dict = rss_reader.rss_to_dict(str(response.content, 'utf-8'))
        if keywords and keywords.split():
            return list(rss_reader.search_by_keywords(keywords.split(), rss_feed_dict))

        return rss_feed_dict.get('items', [])


if __name__ == '__main__':
    cherrypy.tree.mount(Root(), '/', 'app.conf')

    cherrypy.engine.start()
    cherrypy.engine.block()
