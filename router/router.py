from flask import Blueprint, Response
import json

main_router = Blueprint('main_router', __name__,)

@main_router.route('/test', methods=["GET"])
def test_get():
    message = {'hello': 'there'}
    message = json.dumps(message)
    return Response(response=message, status=200, mimetype='application/json')