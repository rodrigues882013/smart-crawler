import json

import requests as http
from config import settings
from lxml import etree
from bs4 import BeautifulSoup


class AppService(object):

    @classmethod
    def get_content_from_url(cls, url=None):
        if url is None:
            url = settings['application']['feed_url']

        resp = http.get(url)

        if resp.status_code == 200:
            return resp.content

    @classmethod
    def build_xml(cls, content):
        try:
            return etree.fromstring(content)
        except Exception as e:
            pass

    @classmethod
    def parse_content(cls, content, content_type='xml'):
        if content_type == 'xml':
            return cls.build_xml(content)

    @classmethod
    def xml_to_json(cls, content):
        soup = BeautifulSoup(content, 'lxml')
        feed = dict(feed=list())
        for i in soup.findAll('item'):
            feed['feed'].append(
                dict(
                    title=i.title.find(text=True),
                    link=i.link.find(text=True),
                    description=[
                        dict(type='text', content=list(map(lambda x:  ''.join(x.findAll(text=True)), i.description.findAll('p')))),
                        dict(type='link', content=list(map(lambda x: x.get('href'), i.description.findAll('a')))),
                        dict(type='image', content=list(map(lambda x: x.get('src'), i.description.findAll('img'))))
            ]))

        return json.dumps(feed)
