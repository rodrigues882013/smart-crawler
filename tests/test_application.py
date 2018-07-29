import unittest

from feed_api.feed.service import FeedService


class AppTest(unittest.TestCase):

    def test_if_get_content_from_url_exist(self):
        self.assertTrue(hasattr(FeedService, 'get_content_from_url'))

    def test_if_xml_to_json(self):
        self.assertTrue(hasattr(FeedService, 'xml_to_json'))

    def test_if_get_content(self):
        self.assertTrue(hasattr(FeedService, 'get_content'))

    def test_get_content(self):
        self.assertEqual(FeedService.get_content('<link>Hello World</link>', r'<link>(.*?)</link>', 0), 'Hello World')

        self.assertEqual(FeedService.get_content('<title>Hello World</title><name>Test</name><title>New Hello '
                                                 'World</title><name>Teste 2</name>', r'<title>(.*?)</title>', 1),
                         'New Hello World')


if __name__ == '__main__':
    unittest.main()
