
from flask import request, jsonify, Blueprint, current_app as app
from feed_api.auth.service import requires_auth
from flask_restful import Resource, Api

from feed_api.decorators import logger_gunicorn
from .service import FeedService as service

feed_bp = Blueprint('feed_bp', __name__)
api = Api(feed_bp)


class Feed(Resource):

    @requires_auth
    @logger_gunicorn
    def get(self):
        app.logger.info("Retrieve feed from url: %s", app.config['FEED_URL'])
        content = service.get_content_from_url(app.config['FEED_URL'])
        return jsonify(service.xml_to_json(content))


api.add_resource(Feed, '/feed')
