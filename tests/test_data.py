test_feed = '''<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet title="XSL_formatting" type="text/xsl" href="/shared/bsp/xsl/rss/nolsol.xsl"?>
<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0" xmlns:media="http://search.yahoo.com/mrss/">
    <channel>
        <title><![CDATA[BBC News - World]]></title>
        <description><![CDATA[BBC News - World]]></description>
        <link>http://www.bbc.co.uk/news/</link>
        <image>
            <url>http://news.bbcimg.co.uk/nol/shared/img/bbc_news_120x60.gif</url>
            <title>BBC News - World</title>
            <link>http://www.bbc.co.uk/news/</link>
        </image>
        <generator>RSS for Node</generator>
        <lastBuildDate>Fri, 20 Jan 2017 13:32:00 GMT</lastBuildDate>
        <copyright><![CDATA[Copyright: (C) British Broadcasting Corporation, see http://news.bbc.co.uk/2/hi/help/rss/4498287.stm for terms and conditions of reuse.]]></copyright>
        <language><![CDATA[en-gb]]></language>
        <ttl>15</ttl>
        <item>
            <title><![CDATA[Rigopiano avalanche: Eight found alive in Italy hotel after two days]]></title>
            <description><![CDATA[Two children are among the eight who have spent at least 40 hours buried in snow and rubble.]]></description>
            <link>http://www.bbc.co.uk/news/world-europe-38691103</link>
            <guid isPermaLink="true">http://www.bbc.co.uk/news/world-europe-38691103</guid>
            <pubDate>Fri, 20 Jan 2017 12:55:28 GMT</pubDate>
            <media:thumbnail width="976" height="549" url="http://c.files.bbci.co.uk/78D0/production/_93682903_hi037382118.jpg"/>
        </item>
        <item>
            <title><![CDATA[Gambia crisis: Jammeh given last chance to resign as troops close in]]></title>
            <description><![CDATA[Regional leaders are in Gambia to persuade Yahya Jammeh to transfer power to his successor.]]></description>
            <link>http://www.bbc.co.uk/news/world-africa-38686144</link>
            <guid isPermaLink="true">http://www.bbc.co.uk/news/world-africa-38686144</guid>
            <pubDate>Fri, 20 Jan 2017 12:45:16 GMT</pubDate>
            <media:thumbnail width="976" height="549" url="http://c.files.bbci.co.uk/9201/production/_93677373_gambia.jpg"/>
        </item>
        <item>
            <title><![CDATA[Syria: IS destroys part of Palmyra's Roman Theatre]]></title>
            <description><![CDATA[IS militants destroy part of the Roman Theatre's facade and a nearby monument.]]></description>
            <link>http://www.bbc.co.uk/news/world-middle-east-38689131</link>
            <guid isPermaLink="true">http://www.bbc.co.uk/news/world-middle-east-38689131</guid>
            <pubDate>Fri, 20 Jan 2017 12:42:59 GMT</pubDate>
            <media:thumbnail width="976" height="549" url="http://c.files.bbci.co.uk/102A/production/_93683140_unosat_palmyra_tetrapylon_amphitheatre_10january2017_dg_wv02.png"/>
        </item>
    </channel>
</rss>'''

test_parsed_dict = {
    'description': 'BBC News - World',
    'published': 'Fri, 20 Jan 2017 13:32:00 GMT',
    'image': 'http://news.bbcimg.co.uk/nol/shared/img/bbc_news_120x60.gif',
    'title': 'BBC News - World',
    'items': [
        {
            'guid': 'world-europe-38691103',
            'thumbnail': 'http://c.files.bbci.co.uk/78D0/production/_93682903_hi037382118.jpg',
            'description': 'Two children are among the eight who have spent at least 40 hours buried in snow and rubble.',
            'link': 'http://www.bbc.co.uk/news/world-europe-38691103',
            'title': 'Rigopiano avalanche: Eight found alive in Italy hotel after two days'
        },
        {
            'guid': 'world-africa-38686144',
            'thumbnail': 'http://c.files.bbci.co.uk/9201/production/_93677373_gambia.jpg',
            'description': 'Regional leaders are in Gambia to persuade Yahya Jammeh to transfer power to his successor.',
            'link': 'http://www.bbc.co.uk/news/world-africa-38686144',
            'title': 'Gambia crisis: Jammeh given last chance to resign as troops close in'
        },
        {
            'guid': 'world-middle-east-38689131',
            'thumbnail': 'http://c.files.bbci.co.uk/102A/production/_93683140_unosat_palmyra_tetrapylon_amphitheatre_10january2017_dg_wv02.png',
            'description': "IS militants destroy part of the Roman Theatre's facade and a nearby monument.",
            'link': 'http://www.bbc.co.uk/news/world-middle-east-38689131',
            'title': "Syria: IS destroys part of Palmyra's Roman Theatre"
        }
    ]
}
