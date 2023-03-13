from flask import Blueprint, jsonify, request, abort
from main import db
from models.corkboard import Corkboard
from models.users import User
from schemas.corkboard_schema import notice_schema, corkboard_schema
from schemas.user_schema import user_schema, users_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

corkboard = Blueprint('corkboard', __name__, url_prefix="/corkboard")

# GET users/ corkboard endpoint

@corkboard.route("/users", methods = ["GET"])
def get_users():
    # get all users from the database table
    users_list = User.query.all()
    result = users_schema.dump(users_list)
    return jsonify(result)

# GET all notices routes endpoint
@corkboard.route("/", methods=["GET"])
def get_corkboard():
    corkboard_list = Corkboard.query.all()
    result = corkboard_schema.dump(corkboard_list)
    return jsonify(result)

# GET single notice by ID endpoint
@corkboard.route("/<int:id>/", methods=["GET"])
def get_notice(id):
    notice = Corkboard.query.filter_by(id=id).first()
    if not notice:
        return abort(400, description = "Notice does not exist")
    result = notice_schema.dump(notice)
    return jsonify(result)

# GET search queries with strings
@corkboard.route("/search", methods=["GET"])
def search_corkboard():
    corkboard_list = []
    if request.args.get('status'):
        corkboard_list = Corkboard.query.filter(Corkboard.status.ilike('%' + request.args.get('status') + '%'))

    result = corkboard_schema.dump(corkboard_list)
    return jsonify(result)

# POST notice endpoint
@corkboard.route("/", methods=["POST"])
@jwt_required()
def create_notice():
    notice_fields = notice_schema.load(request.json)
    user_id = get_jwt_identity()
    new_notice = Corkboard()
    new_notice.date = date.today()
    new_notice.notice = notice_fields["notice"]
    new_notice.description = notice_fields["description"]
    new_notice.status = notice_fields["status"]
    new_notice.user_id = user_id
    db.session.add(new_notice)
    db.session.commit()
    return jsonify(notice_schema.dump(new_notice))

# PUT update notice route endpoint

@corkboard.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_notice(id):
    notice_fields = notice_schema.load(request.json)
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="You're not authorised to do that!")
    # Come back to this, I might not want to restrict this functionality to only admin
    if not user.admin:
        return abort(401, description="You must be an admin to do that!")
    notice = Corkboard.query.filter_by(id=id).first()
    if not notice:
        return abort (400, description = "Notice doesn't exist")
    # update rescue details
    notice.notice = notice_fields["notice"]
    notice.description = notice_fields["description"]
    notice.date = date.today()
    notice.status = notice_fields["status"]
    db.session.commit()
    return jsonify(notice_schema.dump(notice))

# DELETE notice endpoint
@corkboard.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_notice(id):
    notice = Corkboard.query.filter_by(id=id).first()
    if not notice:
        return abort(400, description = "Notice does not exist!")
    db.session.delete(notice)
    db.session.commit()
    return jsonify(notice_schema.dump(notice))