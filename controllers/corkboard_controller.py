from flask import Blueprint, jsonify, request
from main import db
from models.corkboard import Corkboard

corkboard = Blueprint('corkboard', __name__, url_prefix="/corkboard")

# The GET all notices routes endpoint
@corkboard.route("/", methods=["GET"])
def get_notices():
    # notices_list = Corkboard.query.all()
    return "Corkboard Retrieved!"

# The POST notice endpoint
@corkboard.route("/", methods=["POST"])
def create_notice():
    return "Notice Created!"

# The DELETE notice endpoint
@corkboard.route("/<int:id>/", methods=["DELETE"])
def delete_notice(id):
    return "Notice Deleted!"