from main import ma
from marshmallow import fields

class AnimalSchema(ma.Schema):
    class Meta:
        ordered = True
        # Fields to expose. Rescue is not included as animals will be shown always attached to a rescue.
        fields = ("name", "classification", "rescues")
    
    rescues = fields.List(fields.Nested("RescueSchema", only=("name", "classification", "town", "contact_number")))
      
animal_schema = AnimalSchema()
animals_schema = AnimalSchema(many=True)