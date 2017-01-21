import unittest

import test_data

class TestRSSParser(unittest.TestCase):
    def setUp(self):
        self.rss = test_data.test_feed

    def tearDown(self):
        self.rss = None

    def test_turn_feed_from_xml_to_json(self):
        fail('Not implemented yet')
