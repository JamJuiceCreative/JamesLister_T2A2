from main import db


class Rescue(db.Model):
    __tablename__= "rescues"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    classification = db.Column(db.String())
    town = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    animals = db.relationship(
        "Animal",
        backref="rescue",
        cascade="all, delete"
    )