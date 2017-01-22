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

    def test_search_for_article_by_keywords_with_one_keyword(self):
        expected = [self.expected_rss_parsed_dict.get('items')[0]]
        keywords = ['avalanche']

        actual = list(rss_reader.search_by_keywords(keywords, self.expected_rss_parsed_dict))

        self.assertListEqual(expected, actual)

    def test_search_for_article_by_keywords_with_two_keywords(self):
        expected = [self.expected_rss_parsed_dict.get('items')[0], self.expected_rss_parsed_dict.get('items')[1]]
        keywords = ['avalanche', 'Regional']

        actual = list(rss_reader.search_by_keywords(keywords, self.expected_rss_parsed_dict))

        self.assertListEqual(expected, actual)


    def test_search_for_article_by_keywords_with_two_keywords_and_case_does_not_matter(self):
        expected = [self.expected_rss_parsed_dict.get('items')[0], self.expected_rss_parsed_dict.get('items')[1]]
        keywords = ['AVALANCHE', 'regional']

        actual = list(rss_reader.search_by_keywords(keywords, self.expected_rss_parsed_dict))

        self.assertListEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main()
