from main import ma
from marshmallow.validate import Length
from models.users import User
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ['id', 'name', 'email', 'password', 'rescue', 'corkboard']
        load_only = ['password', 'admin']
    #set the password's length to a minimum of 6 characters
    password = ma.String(validate=Length(min=6))
    rescue = fields.List(fields.Nested("RescueSchema", exclude=("user",)))
    corkboard = fields.List(fields.Nested("CorkboardSchema", exclude=("user",)))


user_schema = UserSchema()
users_schema = UserSchema(many=True)