from main import db
# from models.rescues_animals import rescues_animals
class Animal(db.Model):
    __tablename__= "animals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    classification = db.Column(db.String())
    # rescues = db.relationship(
    #     "Rescue",
    #     secondary=rescues_animals,
    #     backref=db.backref("animals", lazy="dynamic")
    # )
