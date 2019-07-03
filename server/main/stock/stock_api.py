from flask import Blueprint, jsonify, request
from flask_api import status

BLUEPRINT = Blueprint('stock-api', __name__, url_prefix='/stocks')


@BLUEPRINT.route('', methods=['GET'])
def 
