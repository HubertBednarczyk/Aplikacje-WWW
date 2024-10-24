from polls.models import Person, Team
from polls.serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

TEAM_NAME = 'Team A'
PERSON_DATA = {
    'name': 'Adam',
    'miesiac_dodania': 1,
    'shirt_size': 'S'
}


def create_team(name):
    return Team.objects.create(name=name)


def create_person(data, team):
    return Person.objects.create(**data, team=team)


def serialize_person(person):
    serializer = PersonSerializer(person)
    return serializer.data


def serialize_to_json(data):
    return JSONRenderer().render(data)


def deserialize_from_json(content):
    stream = io.BytesIO(content)
    return JSONParser().parse(stream)


def validate_and_save_person(data):
    deserializer = PersonSerializer(data=data)
    if deserializer.is_valid():
        deserializer.save()
        return deserializer
    return None


# Tworzenie obiektu Team
team = create_team(TEAM_NAME)

# Tworzenie obiektu Person
person = create_person(PERSON_DATA, team)

# Serializacja Person
person_data = serialize_person(person)
print(person_data)

# Serializacja do JSON
json_content = serialize_to_json(person_data)
print(json_content)

# Deserializacja JSON
deserialized_data = deserialize_from_json(json_content)

# Deserializacja i walidacja
deserializer = validate_and_save_person(deserialized_data)
is_valid = deserializer is not None
print(is_valid)
