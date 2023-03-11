from main import db
from models.rescues_animals import rescues_animals

class Rescue(db.Model):
    __tablename__= "rescues"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    classification = db.Column(db.String())
    town = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    animals = db.relationship(
        "Animal",
        secondary=rescues_animals,
        backref=db.backref("rescues", lazy="dynamic"),
        lazy="dynamic"
    )
    def add_animal(self, animal):
        if animal in self.animals:
            # Update animal attributes
            animal.name = animal.name
            animal.classification = animal.classification
        else:
            # Add new animal to the relationship
            self.animals.append(animal)
            db.session.commit()