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
    if request.args.get('classification'):
        animals_list = Animal.query.join(Animal.rescues).filter(Animal.classification.ilike('%' + request.args.get('classification') + '%')).all()
    elif request.args.get('name'):
        animals_list = Animal.query.join(Animal.rescues).filter(Animal.name.ilike('%' + request.args.get('name') + '%')).all()

    result = animals_schema.dump(animals_list)
    return jsonify(result)

# DELETE animals with no associations
@animals.route("/delete", methods=["DELETE"])
def delete_animals():
    if request.args.get('classification'):
        animals_to_delete = Animal.query \
            .outerjoin(Animal.rescues) \
            .filter(Animal.classification.ilike('%' + request.args.get('classification') + '%')) \
            .filter(Rescue.id == None) \
            .all()
    elif request.args.get('name'):
        animals_to_delete = Animal.query \
            .outerjoin(Animal.rescues) \
            .filter(Animal.name.ilike('%' + request.args.get('name') + '%')) \
            .filter(Rescue.id == None) \
            .all()

    for animal in animals_to_delete:
        db.session.delete(animal)
    db.session.commit()

    return jsonify({'message': f'{len(animals_to_delete)} animals deleted.'})

# DELETE all animals with no associations in "animals_rescues" join table
@animals.route("/delete-all", methods=["DELETE"])
def delete_all_animals():
    animals_to_delete = Animal.query \
        .outerjoin(Animal.rescues) \
        .filter(Rescue.id == None) \
        .all()

    for animal in animals_to_delete:
        db.session.delete(animal)
    db.session.commit()

    return jsonify({'message': f'{len(animals_to_delete)} animals deleted.'})