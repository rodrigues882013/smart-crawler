import unittest

from app.service import AppService


class AppTest(unittest.TestCase):

    def test_if_get_content_from_url_exist(self):
        self.assertTrue(hasattr(AppService, 'get_content_from_url'))

    def test_if_parse_content(self):
        self.assertTrue(hasattr(AppService, 'parse_content'))

    def test_load_feed(self):
        self.assertEqual(AppService.get_content_from_url('http://google.com.br'), "")


if __name__ == '__main__':
    unittest.main()
