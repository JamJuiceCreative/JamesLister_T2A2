from flask import Blueprint, jsonify, request, abort
from main import db
from models.rescues import Rescue
from models.users import User
from schemas.rescue_schema import rescue_schema, rescues_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
rescues = Blueprint('rescues', __name__, url_prefix="/rescues")

# GET all rescues routes endpoint
@rescues.route("/", methods=["GET"])
def get_rescues():
    rescues_list = Rescue.query.all()
    result = rescues_schema.dump(rescues_list)
    return jsonify(result)

# GET single rescue by ID endpoint
@rescues.route("/<int:id>/", methods=["GET"])
def get_rescue(id):
    rescue = Rescue.query.filter_by(id=id).first()
    if not rescue:
        return abort(400, description = "Rescue does not exist")
    result = rescue_schema.dump(rescue)
    return jsonify(result)

# GET search queries with strings
@rescues.route("/search", methods=["GET"])
def search_rescues():
    rescue_list = []
    if request.args.get('classification'):
        rescues_list = Rescue.query.filter_by(classification = request.args.get('classification'))
    elif request.args.get('town'):
        rescues_list = Rescue.query.filter_by(town = request.args.get('town'))

    result = rescues_schema.dump(rescues_list)
    return jsonify(result)

# POST rescue endpoint
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

# PUT update rescue route endpoint

@rescues.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_rescue(id):
    rescue_fields = rescue_schema.load(request.json)
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="You're not authorised to do that!")
    # Come back to this, I might not want to restrict this functionality to only admin
    if not user.admin:
        return abort(401, description="You must be an admin to do that!")
    rescue = Rescue.query.filter_by(id=id).first()
    if not rescue:
        return abort (400, description = "Rescue doesn't exist")
    # update rescue details
    rescue.name = rescue_fields["name"]
    rescue.classification = rescue_fields["classification"]
    rescue.town = rescue_fields["town"]
    db.session.commit()
    return jsonify(rescue_schema.dump(rescue))
    

# DELETE rescue endpoint
@rescues.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_rescue(id):
    rescue = Rescue.query.filter_by(id=id).first()
    if not rescue:
        return abort(400, description = "Rescue does not exist!")
    db.session.delete(rescue)
    db.session.commit()
    return jsonify(rescue_schema.dump(rescue))