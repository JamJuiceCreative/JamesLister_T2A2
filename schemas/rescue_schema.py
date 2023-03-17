from main import ma
from marshmallow import fields


class RescueSchema(ma.Schema):
    class Meta:
        ordered=True
        # Fields to expose
        fields = ("name", "classification", "town", "contact_number", "user", "animals")
    user = fields.Nested("UserSchema", only=("name",))
    animals = fields.List(fields.Nested("AnimalSchema", only=("name",)))

#single rescue schema, when one rescue needs to be retrieved
rescue_schema = RescueSchema()
#multiple rescue schema, when many rescues need to be retrieved
rescues_schema = RescueSchema(many=True)