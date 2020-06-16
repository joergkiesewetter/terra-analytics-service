import os

from flask_compress import Compress
from flask import Flask, current_app, jsonify
from flask_cors import CORS

from controller.data_controller import data_controller
from util.custom_json_encoder import CustomJSONEncoder

COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500

application = Flask(__name__)
Compress(application)
CORS(application)
application.config.from_object(os.environ['APP_SETTINGS'])

application.register_blueprint(data_controller)

application.json_encoder = CustomJSONEncoder

'''
error handling
'''


@application.errorhandler(400)
@application.errorhandler(401)
@application.errorhandler(403)
@application.errorhandler(404)
@application.errorhandler(405)
@application.errorhandler(406)
@application.errorhandler(408)
@application.errorhandler(409)
@application.errorhandler(410)
@application.errorhandler(423)
@application.errorhandler(500)
def error_handling_json(error):
    print(error.description)
    response = jsonify({'message': error.description})
    return response, error.code


if __name__ == "__main__":
    application.run()
