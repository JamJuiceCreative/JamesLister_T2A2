from main import db

class Corkboard(db.Model):
    __tablename__= "corkboard"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date())
    notice = db.Column(db.String())
    description = db.Column(db.String())
    status = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
