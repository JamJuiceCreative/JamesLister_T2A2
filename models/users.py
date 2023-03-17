from main import db
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    rescues = db.relationship(
        "Rescue",
        backref="user",
        cascade="all, delete"
    )
    corkboard = db.relationship(
        "Corkboard",
        backref="user",
        cascade="all, delete"
    )
    responses = db.relationship(
        "Response",
        backref="user",
        cascade="all, delete"
    )