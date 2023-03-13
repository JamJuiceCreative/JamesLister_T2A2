from flask import Blueprint, jsonify, request, abort
from main import db
from models.corkboard import Corkboard
from models.users import User
from schemas.corkboard_schema import corkboards_schema, corkboard_schema
from schemas.user_schema import user_schema, users_schema
from schemas.response_schema import response_schema, responses_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

corkboards = Blueprint('corkboards', __name__, url_prefix="/corkboards")

# GET users/ corkboard endpoint

@corkboards.route("/users", methods = ["GET"])
def get_users():
    # get all users from the database table
    users_list = User.query.options(db.joinedload(User.rescues)).all()
    result = users_schema.dump(users_list)
    return jsonify(result)

# GET all notices routes endpoint
@corkboards.route("/", methods=["GET"])
def get_corkboards():
    corkboards_list = Corkboard.query.all()
    result = corkboards_schema.dump(corkboards_list)
    return jsonify(result)

# GET single notice by ID endpoint
@corkboards.route("/<int:id>/", methods=["GET"])
def get_corkboard(id):
    corkboard = Corkboard.query.filter_by(id=id).first()
    if not corkboard:
        return abort(400, description = "corkboard does not exist")
    result = corkboard_schema.dump(corkboard)
    return jsonify(result)

# GET search queries with strings
@corkboards.route("/search", methods=["GET"])
def search_corkboards():
    corkboards_list = []
    if request.args.get('status'):
        corkboards_list = Corkboard.query.filter(Corkboard.status.ilike('%' + request.args.get('status') + '%'))

    result = corkboards_schema.dump(corkboards_list)
    return jsonify(result)

# POST notice endpoint
@corkboards.route("/", methods=["POST"])
@jwt_required()
def create_corkboard():
    corkboard_fields = corkboard_schema.load(request.json)
    user_id = get_jwt_identity()
    new_corkboard = Corkboard()
    new_corkboard.date = date.today()
    new_corkboard.notice = corkboard_fields["notice"]
    new_corkboard.description = corkboard_fields["description"]
    new_corkboard.status = corkboard_fields["status"]
    new_corkboard.user_id = user_id
    db.session.add(new_corkboard)
    db.session.commit()
    return jsonify(corkboard_schema.dump(new_corkboard))

#POST a new response
@corkboards.route("/<int:id>/responses", methods=["POST"])
# logged in user required
@jwt_required()
# Corkboard id required to assign the comment to a corkboard
def post_response(id):
    # #Create a new comment
    response_fields = response_schema.load(request.json)

    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return abort(401, description="Invalid user")

    # find the corkboard notice
    corkboard = Corkboard.query.filter_by(id=id).first()
    #return an error if the card doesn't exist
    if not corkboard:
        return abort(400, description= "Corkboard notice does not exist")
    #create the response with the given values
    new_response = Response()
    new_response.response = response_fields["response"]
    # Use the corkboard notice gotten by the id of the route
    new_response.corkboard = corkboard
    # Use that id to set the ownership of the card
    new_response.user_id = user_id
    # add to the database and commit
    db.session.add(new_response)
    db.session.commit()
    #return the card in the response
    return jsonify(corkboard_schema.dump(corkboard))

# PUT update notice route endpoint

@corkboards.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_corkboard(id):
    corkboard_fields = corkboard_schema.load(request.json)
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="You're not authorised to do that!")
    # Come back to this, I might not want to restrict this functionality to only admin
    if not user.admin:
        return abort(401, description="You must be an admin to do that!")
    corkboard = Corkboard.query.filter_by(id=id).first()
    if not corkboard:
        return abort (400, description = "Corkboard doesn't exist")
    # update rescue details
    corkboard.notice = corkboard_fields["notice"]
    corkboard.description = corkboard_fields["description"]
    corkboard.date = date.today()
    corkboard.status = corkboard_fields["status"]
    db.session.commit()
    return jsonify(corkboard_schema.dump(corkboard))

# DELETE notice endpoint
@corkboards.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_corkboard(id):
    corkboard = Corkboard.query.filter_by(id=id).first()
    if not corkboard:
        return abort(400, description = "Corkboard does not exist!")
    db.session.delete(corkboard)
    db.session.commit()
    return jsonify(corkboard_schema.dump(corkboard))