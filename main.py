import logging

from app.service import AppService

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def main():
    content = AppService.get_content_from_url()
    json = AppService.xml_to_json(content)
    logger.info("Result: %s", json)


if __name__ == '__main__':
    main()
