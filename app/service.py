import json
import re

import requests as http
from bs4 import BeautifulSoup

from config import settings


class AppService(object):

    @classmethod
    def get_content_from_url(cls, url=None):
        if url is None:
            url = settings['application']['feed_url']

        resp = http.get(url)

        if resp.status_code == 200:
            return resp.content

    @classmethod
    def generate_text(cls, text_array):
        text = ''
        for x in text_array:
            text += ' ' + x

        return text

    @classmethod
    def get_content(cls, content, pattern, position):
        matches = re.finditer(pattern, str(content), re.MULTILINE)

        idx = 0
        for match in matches:
            if idx == position:
                return match.groups()[0]
            idx += 1

    @classmethod
    def get_link(cls, content, position):
        return cls.get_content(content, r'<link>(.*?)</link>', position)

    @classmethod
    def get_title(cls, content, position):
        return cls.get_content(content, r'<title><!\[CDATA\[(.*?)\]\]></title>', position)

    @classmethod
    def xml_to_json(cls, content):
        soup = BeautifulSoup(content, 'lxml')
        feed = dict(feed=list())

        idx = 0
        for i in soup.findAll('item'):
            feed['feed'].append(dict(item=dict(
                title=cls.get_title(content, idx),
                link=cls.get_link(content, idx),
                description=[
                    dict(type='text', content=cls.generate_text(list(map(lambda x: ''.join(x.findAll(text=True)),
                                                                         i.description.findAll('p'))))),
                    dict(type='link', content=list(map(lambda x: x.get('href'), i.description.findAll('a')))),
                    dict(type='image', content=list(map(lambda x: x.get('src'), i.description.findAll('img'))))
                ])))
            idx += 1

        return json.dumps(feed)
