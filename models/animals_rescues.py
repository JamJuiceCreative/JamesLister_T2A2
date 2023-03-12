from main import db

animals_rescues = db.Table('animals_rescues',
    db.Column('animal_id', db.Integer, db.ForeignKey('animals.id')),
    db.Column('rescue_id', db.Integer, db.ForeignKey('rescues.id'))
)