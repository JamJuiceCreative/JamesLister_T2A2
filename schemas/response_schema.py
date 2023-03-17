from main import ma
from marshmallow import fields

class ResponseSchema(ma.Schema):
    class Meta:
        ordered = True
        # Fields to expose. Corkboard is not included as responses will be shown always attached to a Corkboard notice.
        fields = ("response", "user")
    user =  fields.Nested("UserSchema", only=("name",))  
      
response_schema = ResponseSchema()

responses_schema = ResponseSchema(many=True)