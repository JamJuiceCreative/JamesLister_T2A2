from flask import Blueprint, jsonify, request, abort
from main import db
from models.rescues import Rescue
from models.users import User
from models.animals import Animal
from models.rescues_animals import rescues_animals
from models.animals_rescues import animals_rescues
from schemas.rescue_schema import rescue_schema, rescues_schema
from schemas.user_schema import user_schema, users_schema
from schemas.animal_schema import animal_schema, animals_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
rescues = Blueprint('rescues', __name__, url_prefix="/rescues")

# GET users/ rescues endpoint
@rescues.route("/users", methods = ["GET"])
def get_users():
    # get all users from the database table
    users_list = User.query.all()
    result = users_schema.dump(users_list)
    return jsonify(result)


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
    rescues_list = []
    if request.args.get('classification'):
        rescues_list = Rescue.query.filter(Rescue.classification.ilike('%' + request.args.get('classification') + '%'))
    elif request.args.get('town'):
        rescues_list = Rescue.query.filter(Rescue.town.ilike('%' + request.args.get('town') + '%'))

    result = rescues_schema.dump(rescues_list)
    return jsonify(result)

# POST new rescue endpoint
@rescues.route("/", methods=["POST"])
@jwt_required()
def create_rescue():
    # #Create a new rescue
    rescue_fields = rescue_schema.load(request.json)

    # get the id from jwt
    user_id = get_jwt_identity()
    new_rescue = Rescue()
    new_rescue.name = rescue_fields["name"]
    new_rescue.classification = rescue_fields["classification"]
    new_rescue.town = rescue_fields["town"]
    # Use that id to set the ownership of the rescue org
    new_rescue.user_id = user_id
    # add to the database and commit
    db.session.add(new_rescue)
    db.session.commit()
    return jsonify(rescue_schema.dump(new_rescue))

# POST add an animal/ classification to a rescue organisation
@rescues.route("/<int:id>/animals", methods=["POST"])
# logged in user required
@jwt_required()
# rescue id is required to add an animal
def add_animal(id):
    # #Create a new comment
    animal_fields = animal_schema.load(request.json)

    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    if not user:
        return abort(401, description="You're not allowed to do that!")
    # find the rescue
    rescue = Rescue.query.filter_by(id=id).first()
    #return an error if the rescue doesn't exist
    if not rescue:
        return abort(400, description= "Rescue organisation not in database")
    # check if the animal already exists in the database
    animal = Animal.query.filter_by(name=animal_fields["name"]).first()
    if animal:
    # check if the relationship already exists in the rescues_animals table
        existing_relationship = db.session.query(rescues_animals).filter_by(animal_id=animal.id, rescue_id=rescue.id).first()
        if existing_relationship:
            return jsonify(({"message": "This animal has already been associated with this rescue"}))
        else:
            # if relationship does not exist, add a new one to the rescues_animals table
            rescues_animals_query = rescues_animals.insert().values(animal_id=animal.id, rescue_id=rescue.id)
            db.session.execute(rescues_animals_query)       
            #also add one to the animals_rescues table
            animals_rescues_query = animals_rescues.insert().values(rescue_id=rescue.id, animal_id=animal.id)
            db.session.execute(animals_rescues_query)
            # update the animal classification
            animal.classification = animal_fields["classification"]
            db.session.commit()
        # return the animal in the response
        return jsonify(animal_schema.dump(animal,))
    else:
        #create the Animal with the given values
        new_animal = Animal()
        new_animal.name = animal_fields["name"]
        new_animal.classification = animal_fields["classification"]
        # Use the rescue gotten by the id of the route
        new_animal.rescue = [rescue]
        # Use that id to set the ownership of the rescue org
        new_animal.user_id = user_id
        # add to the database and commit
        db.session.add(new_animal)
        db.session.commit()
        # add the new rescues animals association to the rescues_animals table
        # add the new rescue rescues animals association to the animals_rescue table
        animals_rescues_query = animals_rescues.insert().values(rescue_id=rescue.id, animal_id=new_animal.id)
        db.session.execute(animals_rescues_query)
        db.session.commit()
        
        #return the new animal in the response
        return jsonify(animal_schema.dump(new_animal,))

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
    

# DELETE delete an animal from a rescue organisation
@rescues.route("/<int:id>/animals", methods=["DELETE"])
# logged in user required
@jwt_required()
# rescue id is required to delete an animal
def delete_animal(id):
    # get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find it in the db
    user = User.query.get(user_id)
    # Make sure it is in the database
    if not user:
        return abort(401, description="You're not authorised to do that!")
    # find the rescue
    rescue = Rescue.query.filter_by(id=id).first()
    # return an error if the rescue doesn't exist
    if not rescue:
        return abort(400, description="Rescue organisation not in database!")
    # get the animal name from the request body
    animal_name = request.json.get("name", None)
    # check if the animal exists in the rescue
    animal = Animal.query.filter(Animal.name.ilike(animal_name)).filter(Animal.rescues.any(id=id)).first()
    if not animal:
        return abort(400, description="Animal not found in rescue organisation")
    # check if the animal is associated with any other rescues
    other_rescues = animal.rescues.filter(Rescue.id != id).all()
    if other_rescues:
        # if the animal is associated with other rescues, remove the association with this rescue
        animal.rescues.remove(rescue)
        db.session.commit()
    else:
        # if the animal is not associated with any other rescues, delete it from the animals table
        db.session.delete(animal)
        db.session.commit()
    # delete the association from the rescues_animals table
    rescues_animals_query = rescues_animals.delete().where(
        rescues_animals.c.animal_id == animal.id and rescues_animals.c.rescue_id == rescue.id)
    db.session.execute(rescues_animals_query)
    db.session.commit()
    # delete the association from the animals_rescues table
    animals_rescues_query = animals_rescues.delete().where(
        animals_rescues.c.rescue_id == rescue.id and animals_rescues.c.animal_id == animal.id)
    db.session.execute(animals_rescues_query)
    db.session.commit()
    return jsonify({"message": "Animal deleted from rescue organisation"})