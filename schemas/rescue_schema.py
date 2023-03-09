from main import ma

class RescueSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "classification", "town")

#single card schema, when one card needs to be retrieved
rescue_schema = RescueSchema()
#multiple card schema, when many cards need to be retrieved
rescues_schema = RescueSchema(many=True)