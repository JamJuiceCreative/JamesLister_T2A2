from main import ma
from marshmallow import fields

class RescueSchema(ma.Schema):
    class Meta:
        ordered=True
        # Fields to expose
        fields = ("id", "name", "classification", "town", "user", "animals")
    user = fields.Nested("UserSchema", only=("name",))
    animals = fields.List(fields.Nested("AnimalSchema"))

#single card schema, when one card needs to be retrieved
rescue_schema = RescueSchema()
#multiple card schema, when many cards need to be retrieved
rescues_schema = RescueSchema(many=True)