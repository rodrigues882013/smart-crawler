from flask import request, jsonify, Blueprint
from feed_api.auth.service import requires_auth
from flask_restful import Resource, Api
from .service import FeedService as service

feed_bp = Blueprint('feed_bp', __name__)
api = Api(feed_bp)


class Feed(Resource):

    @requires_auth
    def get(self):
        content = service.get_content_from_url('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
        return jsonify(service.xml_to_json(content))


api.add_resource(Feed, '/feed')
