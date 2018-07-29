import unittest
import json
from app.service import AppService


class AppTest(unittest.TestCase):

    def test_if_get_content_from_url_exist(self):
        self.assertTrue(hasattr(AppService, 'get_content_from_url'))

    def test_if_xml_to_json(self):
        self.assertTrue(hasattr(AppService, 'xml_to_json'))

    def test_if_get_content(self):
        self.assertTrue(hasattr(AppService, 'get_content'))

    def test_if_get_link(self):
        self.assertTrue(hasattr(AppService, 'get_link'))

    def test_if_get_title(self):
        self.assertTrue(hasattr(AppService, 'get_title'))

    def test_if_generate_text(self):
        self.assertTrue(hasattr(AppService, 'generate_text'))

    def test_generate_text(self):
        self.assertEqual(AppService.generate_text(['Hello', 'World']), ' Hello World')
        self.assertEqual(AppService.generate_text(['Todavia,', 'o', 'início', 'da', 'atividade', 'geral']),
                         ' Todavia, o início da atividade geral')

    def test_get_link(self):
        self.assertEqual(
            AppService.get_link('<link>Hello World</link><link>No Hello World</link>', 0), 'Hello World')
        self.assertEqual(
            AppService.get_link('<link>Hello World</link><link>No Hello World</link>', 1), 'No Hello World')
        self.assertNotEqual(
            AppService.get_link('<link>Hello World</link><link>No Hello World</link>', 0), 'No Hello World')

    def test_get_title(self):
        self.assertEqual(
            AppService.get_title('<title><![CDATA[Hello World]]></title><title><![CDATA[No Hello World]]></title>', 0),
            'Hello World')
        self.assertEqual(
            AppService.get_title('<title><![CDATA[Hello World]]></title><title><![CDATA[No Hello World]]></title>', 1),
            'No Hello World')
        self.assertNotEqual(
            AppService.get_title('<title><![CDATA[Hello World]]></title><title><![CDATA[No Hello World]]></title>', 0),
            'No Hello World')

    def test_get_content(self):
        self.assertEqual(AppService.get_content('<link>Hello World</link>', r'<link>(.*?)</link>', 0), 'Hello World')

        self.assertEqual(AppService.get_content('<title>Hello World</title><name>Test</name><title>New Hello '
                                                 'World</title><name>Teste 2</name>', r'<title>(.*?)</title>', 1),
                         'New Hello World')

    def test_xml_to_json(self):
        xml = '<item>' \
              '<title><![CDATA[Ford Ka e VW Gol automáticos]]></title>' \
              '<description>' \
              '<p>No programa <strong>DRIVE</strong> dessa semana<a href="google.com.br">Click aqui </a><img ' \
              'src="image.jpg"/></p>' \
              '</description>' \
              '</item>' \
              '<link>google.com.br</link>'

        feed = '{"feed": [{"item": {"title": "Ford Ka e VW Gol automáticos", "link": "google.com.br", "description": [{' \
               '"type": "text", "content": " No programa DRIVE dessa semanaClick aqui "}, {"type": "link", "content": [' \
               '"google.com.br"]}, {"type": "image", "content": ["image.jpg"]}]}}]}'
        self.assertEqual(AppService.xml_to_json(xml), feed)


if __name__ == '__main__':
    unittest.main()
