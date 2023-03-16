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
    other_rescues = animal.rescues.filter(Rescue.id < id).all()
    if other_rescues:
        # if the animal is associated with other rescues, remove the association with this rescue
        animal.rescues.remove(rescue)
        db.session.commit()
    else:
        # if the animal is not associated with any other rescues, delete it from the animals table
        db.session.delete(animal)
        db.session.commit()
    print(rescue.id)
    print(animal.id)
    # delete the association from the rescues_animals table
    rescues_animals_query = rescues_animals.delete().where(
        rescues_animals.c.animal_id == animal.id and rescues_animals.c.rescue_id == rescue.id)
    db.session.execute(rescues_animals_query)
    db.session.commit()

    # delete the association from the animals_rescues table
    animals_rescues_query = animals_rescues.delete().where(
        animals_rescues.c.animal_id == animal.id and animals_rescues.c.rescue_id == rescue.id)
    db.session.execute(animals_rescues_query)
    db.session.commit()
    return jsonify({"message": "Animal deleted from rescue organisation"})