from main import ma
from marshmallow import fields

class CorkboardSchema(ma.Schema):
    class Meta:
        ordered = True
        # Fields to expose
        fields = ("date", "notice", "where", "description", "status", "user", "rescue", "responses")
    user = fields.Nested("UserSchema", only=("name",))
    rescue = fields.Nested("RescueSchema", only=("id", "name"))
    responses = fields.List(fields.Nested("ResponseSchema"))

#single card schema, when one card needs to be retrieved
corkboard_schema = CorkboardSchema()
#multiple card schema, when many cards need to be retrieved
corkboards_schema = CorkboardSchema(many=True)