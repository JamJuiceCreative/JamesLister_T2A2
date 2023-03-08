from main import db

class Corkboard(db.Model):
    __tablename__= "corkboard"
    id = db.Column(db.Integer, primary_key=True)
    notice = db.Column(db.String())
    description = db.Column(db.String())
    date_posted = db.Column(db.Date())
    date_of = db.Column(db.Date())
    status = db.Column(db.String())