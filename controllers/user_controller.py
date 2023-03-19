from flask import Blueprint, jsonify, request, abort
from main import db
# from models.rescues import Rescue
from models.users import User
# from models.animals import Animal
# from models.rescues_animals import rescues_animals
# from models.animals_rescues import animals_rescues
# from schemas.rescue_schema import rescue_schema, rescues_schema
from schemas.user_schema import user_schema, users_schema
# from schemas.animal_schema import animal_schema, animals_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
users = Blueprint('users', __name__, url_prefix="/users")

# GET users/ rescues endpoint
# *This returns all users in database and displays their associated rescues (if any). 
@users.route("/", methods = ["GET"])
def get_users():
    # get all users from the database table
    users_list = User.query.all()
    result = users_schema.dump(users_list)
    return jsonify(result)


# DELETE user by ID endpoint
# *Deletes user and all associated data, requires bearer token and can only be performed by the user themselves or the admin. Also deletes associated corkboards and rescues. (Doesn't delete associated animals as generally they will always be associated with other rescues)
@users.route("/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="You're not authorized to do that!")
    if user.admin:
        user_to_delete = User.query.get(id)
        if not user_to_delete:
            return abort(400, description="User doesn't exist!")
    else:
        if not user:
            return abort(401, description="You're not authorized to do that!")
        if user.id != id:
            return abort(401, description="You're not authorized to delete this user!")
        user_to_delete = user
    
    db.session.delete(user_to_delete)
    db.session.commit()
    response = {
        "message": "User deleted from database!"
    }
    return (response), 200
