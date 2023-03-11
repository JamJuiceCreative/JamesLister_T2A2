from main import db

class Animal(db.Model):
    __tablename__= "animals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    classification = db.Column(db.String())