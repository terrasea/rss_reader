import feedparser

def rss_to_dict(rawrss):
    '''
    Turns raw RSS into a dictionary

    returns a dict with keys of 'title', 'description', 'image', 'published' and 'items'.
    'items' are a list of dicts with each entry having the keys of 'title', 'link', 'description' and 'thumbnail'. Each item represents an article. The 'thumbnail' is the url of the thumbnail image for the article.
    '''
    # strip to get rid of spaces at front and end of XML
    # which will fail to parse, if present
    raw_dict = feedparser.parse(rawrss.strip())

    processed = {
        'title': raw_dict.feed.title,
        'description': raw_dict.feed.description,
        'image': raw_dict.feed.image.url,
        'published': raw_dict.feed.updated,
        'items': [{'guid': x.guid.split('/').pop(), 'title': x.title, 'link': x.link, 'description': x.description, 'thumbnail': x.media_thumbnail[0].get('url') if x.media_thumbnail else ''} for x in raw_dict.entries]
        }

    return processed
    
def search_by_keywords(keywords_list, rss_dict):
    '''
    Searches items in RSS feed dictionary for the pressence of any of the supplied list of keywords in the list of items (articles), returning a generator for a list of items (articles), which has at least one of the search keywords in either the title or the description
    '''
    return (item for item in rss_dict.get('items', []) if any((True for word in keywords_list if word.lower() in item.get('title', '').lower() or word.lower() in item.get('description', '').lower())))


def get_article(guid, raw_dict):
    items = [item for item in raw_dict.get('items', []) if item.get('guid') == guid]

    return items.pop() if items else {}
