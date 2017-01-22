import unittest
import unittest.mock

import test_data
import rss_reader


class TestRSSReader(unittest.TestCase):
    def setUp(self):
        self.rss = test_data.test_feed
        self.expected_rss_parsed_dict = test_data.test_parsed_dict

    def tearDown(self):
        self.rss = None

    def test_turn_feed_from_xml_to_dict(self):
        rss_dict = rss_reader.rss_to_dict(self.rss)

        self.assertTrue(isinstance(rss_dict, dict))
        self.assertDictEqual(rss_dict, self.expected_rss_parsed_dict)

if __name__ == '__main__':
    unittest.main()
