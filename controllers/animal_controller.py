from flask import Blueprint, jsonify, request, abort
from main import db
from models.animals import Animal
from models.rescues import Rescue
from schemas.animal_schema import animal_schema, animals_schema
from schemas.rescue_schema import rescue_schema, rescues_schema

animals = Blueprint('animals', __name__, url_prefix="/animals")

# GET all animals endpoint

@animals.route("/", methods = ["GET"])
def get_animals():
    # get all users from the database table
    animals_list = Animal.query.all()
    result = animals_schema.dump(animals_list)
    return jsonify(result)

# GET all animals with associated rescues endpoint
@animals.route("/rescues", methods = ["GET"])
def get_animals_rescues():
    animals = Animal.query.all()
    result = animals_schema.dump(animals)
    for animal in result:
        rescue_id = animal['id']
        rescue = Rescue.query.filter_by(id=rescue_id).first()
        animal['rescue']=rescue_schema.dump(rescue)
    return jsonify(result)

# Get animal by ID
@animals.route("/<int:id>/", methods=["GET"])
def get_animal(id):
    animal = Animal.query.filter_by(id=id).first()
    if not animal:
        return abort(400, description = "Animal does not exist")
    result = animal_schema.dump(animal)
    return jsonify(result)

# search for rescues by animal association
# GET search queries with strings
@animals.route("/search", methods=["GET"])
def search_rescues():
    animals_list = []
    if request.args.get('name'):
        animals_list = Animal.query.filter_by(name = request.args.get('name'))
    elif request.args.get('classification'):
        animals_list = Animal.query.filter_by(classification = request.args.get('classification'))

    result = animals_schema.dump(animals_list)
    return jsonify(result)