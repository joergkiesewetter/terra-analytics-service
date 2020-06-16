import json
import os
import traceback
from datetime import datetime

from flask import Blueprint, request, current_app, jsonify
from werkzeug.exceptions import abort

data_controller = Blueprint('data_controller', __name__)

@data_controller.route('/data/general', methods=['GET'])
def get_data_general():
    try:
        date_string = request.args.get('date')
        date = datetime.strptime(date_string, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    file_path = os.path.join(current_app.config['PATH_GENERAL'], date_string + '.json')

    if not os.path.isfile(file_path):
        abort(404, 'data not found')

    with open(file_path, 'r') as file:
        return jsonify(json.load(file))


@data_controller.route('/data/payments', methods=['GET'])
def get_data_payments():
    try:
        date_string = request.args.get('date')
        date = datetime.strptime(date_string, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    file_path = os.path.join(current_app.config['PATH_PAYMENTS'], date_string + '.json')

    if not os.path.isfile(file_path):
        abort(404, 'data not found')

    with open(file_path, 'r') as file:
        return jsonify(json.load(file))


@data_controller.route('/data/transactions', methods=['GET'])
def get_data_transactions():
    try:
        date_string = request.args.get('date')
        date = datetime.strptime(date_string, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    file_path = os.path.join(current_app.config['PATH_TRANSACTIONS'], date_string + '.json')

    if not os.path.isfile(file_path):
        abort(404, 'data not found')

    with open(file_path, 'r') as file:
        return jsonify(json.load(file))


@data_controller.route('/data/user', methods=['GET'])
def get_data_user():
    try:
        date_string = request.args.get('date')
        date = datetime.strptime(date_string, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    file_path = os.path.join(current_app.config['PATH_USER'], date_string + '.json')

    if not os.path.isfile(file_path):
        abort(404, 'data not found')

    with open(file_path, 'r') as file:
        return jsonify(json.load(file))