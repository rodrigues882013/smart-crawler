import requests as http
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
    def parse_content(cls, content, content_type='xml'):
        pass

