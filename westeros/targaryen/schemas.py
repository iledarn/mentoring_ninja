from ninja import Schema, ModelSchema
from targaryen.models import Person


class DragonOut(Schema):
    name: str
    birth_year: int


class PersonOut(ModelSchema):
    first_name: str
    class Config:
        model = Person
        model_fields = ["id", "birth_year"]
