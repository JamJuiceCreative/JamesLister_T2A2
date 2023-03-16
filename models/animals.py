from main import db
from models.animals_rescues import animals_rescues
class Animal(db.Model):
    __tablename__= "animals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    classification = db.Column(db.String())
    rescues = db.relationship(
        "Rescue",
        secondary=animals_rescues,
        backref=db.backref("animal", lazy="dynamic"),
        lazy="dynamic"
    )
    def add_rescue(self, rescue):
        if rescue in self.rescues:
            # Update animal attributes
            rescue.name = rescue.name
            rescue.classification = rescue.classification
        else:
            # Add new animal to the relationship
            self.rescues.append(rescue)
            db.session.commit()