from flask import Blueprint, jsonify, request, abort
from main import db
from models.corkboard import Corkboard
from schemas.corkboard_schema import notice_schema, corkboard_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

corkboard = Blueprint('corkboard', __name__, url_prefix="/corkboard")

# The GET all notices routes endpoint
@corkboard.route("/", methods=["GET"])
def get_corkboard():
    corkboard_list = Corkboard.query.all()
    result = corkboard_schema.dump(corkboard_list)
    return jsonify(result)

# The POST notice endpoint
@corkboard.route("/", methods=["POST"])
@jwt_required()
def create_notice():
    notice_fields = notice_schema.load(request.json)
    new_notice = Corkboard()
    new_notice.date = date.today()
    new_notice.notice = notice_fields["notice"]
    new_notice.description = notice_fields["description"]
    new_notice.status = notice_fields["status"]
    db.session.add(new_notice)
    db.session.commit()
    return jsonify(notice_schema.dump(new_notice))

# The DELETE notice endpoint
@corkboard.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_notice(id):
    notice = Corkboard.query.filter_by(id=id).first()
    if not notice:
        return abort(400, description = "Notice does not exist!")
    db.session.delete(notice)
    db.session.commit()
    return jsonify(notice_schema.dump(notice))