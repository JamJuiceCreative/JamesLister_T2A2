from main import ma
from marshmallow import fields

class AnimalSchema(ma.Schema):
    class Meta:
        ordered = True
        # Fields to expose. Rescue is not included as animals will be shown always attached to a rescue.
        fields = ("id", "name", "classification", "rescue")
    rescue =  fields.List(fields.Nested("RescueSchema", exclude=('animals',)))
    # check if i can return the rescue data along with the animal classification
      
animal_schema = AnimalSchema()
animals_schema = AnimalSchema(many=True)