from main import ma
# from marshmallow import fields
from models.animals_rescues import AnimalsRescues

class RescuesAnimalsSchema(ma.Schema):
    class Meta:
        model = AnimalsRescues
        fields = ('id', 'animal_id', 'rescue_id')