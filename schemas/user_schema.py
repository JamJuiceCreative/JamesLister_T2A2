from main import ma
from marshmallow.validate import Length
from models.users import User
from marshmallow import fields
from schemas.rescue_schema import RescueSchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        ordered = True
        fields = ['id', 'name', 'email', 'password', 'rescues', 'corkboard']
        load_only = ['password', 'admin']
    password = ma.String(validate=Length(min=6))
    corkboard = fields.List(fields.Nested("CorkboardSchema", exclude=("user",)))
    rescues = fields.List(fields.Nested(RescueSchema, only=("name",)))
    @staticmethod
    def load_rescues(user):
        return user.rescues

user_schema = UserSchema()
users_schema = UserSchema(many=True)