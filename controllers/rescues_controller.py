from flask import Blueprint, jsonify, request, abort
from main import db
from models.rescues import Rescue
from schemas.rescue_schema import rescue_schema, rescues_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
rescues = Blueprint('rescues', __name__, url_prefix="/rescues")

# The GET all rescues routes endpoint
@rescues.route("/", methods=["GET"])
def get_rescues():
    rescues_list = Rescue.query.all()
    result = rescues_schema.dump(rescues_list)
    return jsonify(result)

# The POST rescue endpoint
@rescues.route("/", methods=["POST"])
@jwt_required()
def create_rescue():
    rescue_fields = rescue_schema.load(request.json)
    new_rescue = Rescue()
    new_rescue.name = rescue_fields["name"]
    new_rescue.classification = rescue_fields["classification"]
    new_rescue.town = rescue_fields["town"]
    db.session.add(new_rescue)
    db.session.commit()
    return jsonify(rescue_schema.dump(new_rescue))

# The DELETE rescue endpoint
@rescues.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_rescue(id):
    rescue = Rescue.query.filter_by(id=id).first()
    if not rescue:
        return abort(400, description = "Rescue does not exist!")
    db.session.delete(rescue)
    db.session.commit()
    return jsonify(rescue_schema.dump(rescue))