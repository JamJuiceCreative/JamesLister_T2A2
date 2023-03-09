from main import ma


class CorkboardSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "date", "notice", "description", "status")

#single card schema, when one card needs to be retrieved
notice_schema = CorkboardSchema()
#multiple card schema, when many cards need to be retrieved
corkboard_schema = CorkboardSchema(many=True)