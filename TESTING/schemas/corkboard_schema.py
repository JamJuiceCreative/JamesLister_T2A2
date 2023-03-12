from main import ma
from marshmallow import fields

class CorkboardSchema(ma.Schema):
    class Meta:
        ordered = True
        # Fields to expose
        fields = ("id", "date", "notice", "description", "status", "user")
    user = fields.Nested("UserSchema", only=("name",))

#single card schema, when one card needs to be retrieved
notice_schema = CorkboardSchema()
#multiple card schema, when many cards need to be retrieved
corkboard_schema = CorkboardSchema(many=True)