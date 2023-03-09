from main import ma
from marshmallow import fields

class AnimalSchema(ma.Schema):
    class Meta:
        ordered = True
        # Fields to expose. Card is not included as comments will be shown always attached to a Card.
        fields = ("id", "name", "classification", "rescue")
    rescue =  fields.Nested("RescueSchema", only=("name",))
    # check if i can return the rescue data along with the animal classification
      
animal_schema = AnimalSchema()

animals_schema = AnimalSchema(many=True)