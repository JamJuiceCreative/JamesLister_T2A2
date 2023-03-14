from main import db

class Response(db.Model):
    # define the table name for the db
    __tablename__= "responses"

    id = db.Column(db.Integer,primary_key=True)
    # Add the rest of the attributes. 
    response= db.Column(db.String())
    # two foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    corkboard_id = db.Column(db.Integer, db.ForeignKey("corkboards.id"), nullable=False)
    