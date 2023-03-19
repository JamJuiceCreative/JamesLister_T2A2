from flask import Blueprint, jsonify, request, abort
from main import db
from models.animals import Animal
from models.rescues import Rescue
from schemas.animal_schema import animal_schema, animals_schema
from schemas.rescue_schema import rescue_schema, rescues_schema

animals = Blueprint('animals', __name__, url_prefix="/animals")

# GET all animals endpoint
# *This returns all animals in the database along with their classification and associated rescue information.

@animals.route("/", methods = ["GET"])
def get_animals():
    # get all users from the database table
    animals_list = Animal.query.all()
    result = animals_schema.dump(animals_list)
    return jsonify(result)

# Get animal by ID
# *This returns the animal in the database corresponding to the animal ID. Returns all associated rescue information.
@animals.route("/<int:id>/", methods=["GET"])
def get_animal(id):
    animal = Animal.query.filter_by(id=id).first()
    if not animal:
        return abort(400, description = "Animal does not exist")
    result = animal_schema.dump(animal)
    return jsonify(result)

# search for rescues by animal association
# GET search queries with strings
# *This allows user to search for animals by name or classification and is case insensitive. Returns the animal and classification along with any rescue details it's associated with.
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
# *This allows user to clean up the animals table in the unlikely scenario that enough rescues are deleted that there are no longer any association of rescues with that animal.
# This part of the clean up method can be performed by search query and will delete all unassociated animals according to name or classification.
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
# *Again, it would be uncommon for an animal to longer be associated with a rescue. This method will clean up all of the data from the animals table if in case there are stray animals no longer associated with any rescues.
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