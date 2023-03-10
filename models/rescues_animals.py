from main import db

class RescuesAnimals(db.Model):
    __tablename__ = 'rescues_animals'
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'), primary_key=True)
    rescue_id = db.Column(db.Integer, db.ForeignKey('rescues.id'), primary_key=True)
