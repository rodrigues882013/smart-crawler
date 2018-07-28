from app.service import AppService


def main():
    content = AppService.get_content_from_url('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
    json = AppService.xml_to_json(content)
    print(json)


if __name__ == '__main__':
    main()
