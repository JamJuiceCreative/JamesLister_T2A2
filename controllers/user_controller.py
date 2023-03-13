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
@users.route("/", methods = ["GET"])
def get_users():
    # get all users from the database table
    users_list = User.query.all()
    result = users_schema.dump(users_list)
    return jsonify(result)