import feedparser

def rss_to_dict(rawrss):
    # strip to get rid of spaces at front and end of XML
    # which will fail to parse, if present
    raw_dict = feedparser.parse(rawrss.strip())

    processed = {
        'title': raw_dict.feed.title,
        'description': raw_dict.feed.description,
        'image': raw_dict.feed.image.url,
        'published': raw_dict.feed.updated,
        'items': [{'title': x.title, 'link': x.link, 'description': x.description, 'thumbnail': x.media_thumbnail[0].get('url') if x.media_thumbnail else ''} for x in raw_dict.entries]
        }

    return processed
    
