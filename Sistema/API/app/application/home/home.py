from flask import Blueprint
from flask import current_app as app
from flask import Response

# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__
)


@home_bp.route('/home', methods=['GET'])
def home():
    return Response("home",headers=dict({
  "HeaderExample": "HeaderContent"
}))