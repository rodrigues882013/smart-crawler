import unittest

from app.service import AppService
from lxml import etree


class AppTest(unittest.TestCase):

    def test_if_get_content_from_url_exist(self):
        self.assertTrue(hasattr(AppService, 'get_content_from_url'))

    def test_if_parse_content(self):
        self.assertTrue(hasattr(AppService, 'parse_content'))

    def test_if_build_xml_document(self):
        self.assertTrue(hasattr(AppService, 'parse_content'))

    def test_if_xml_to_json(self):
        self.assertTrue(hasattr(AppService, 'xml_to_json'))

    def test_load_feed(self):
        self.assertEqual(AppService.get_content_from_url('http://google.com.br'), "")

    def test_parse_content(self):
        element = b'<monster name="Heffalump"><trail>Woozle</trail><eeyore mood="boggy"/></monster>'
        doc = AppService.parse_content(element)
        self.assertEqual(etree.tostring(doc), element)


if __name__ == '__main__':
    unittest.main()
