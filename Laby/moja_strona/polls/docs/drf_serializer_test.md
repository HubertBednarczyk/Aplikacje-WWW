# Testowanie serializerów Django Rest Framework

## Testowanie PersonSerializer

```python
from ankiety.models import Person, Team
from ankiety.serializers import PersonSerializer, TeamModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# Tworzenie obiektu Person
team = Team.objects.create(name='Team A')
person = Person(name='Adam', miesiac_dodania=1, team=team)
person.save()

# Serializacja Person
serializer = PersonSerializer(person)
print(serializer.data)
# Oczekiwany output:
# {'id': 1, 'name': 'Adam', 'shirt_size': 'S', 'miesiac_dodania': 1, 'team': 1}

# Serializacja do JSON
content = JSONRenderer().render(serializer.data)
print(content)
# Oczekiwany output
# b'{"id":1,"name":"Adam","shirt_size":"S","miesiac_dodania":1,"team":1}'

# Deserializacja JSON
stream = io.BytesIO(content)
data = JSONParser().parse(stream)

# Deserializacja i walidacja
deserializer = PersonSerializer(data=data)
print(deserializer.is_valid())  # powinna być True

# Walidacja udana, zapis danych
deserializer.save()
```

### Krok 6: Uruchamianie konsoli Django

Możesz uruchomić powyższe testy w konsoli Django, przekazując plik jako potok wejściowy. Na przykład, jeśli zapisałeś kod testujący w pliku `test_serializers.py`:

```bash
python manage.py shell < ./ankiety/docs/test_serializers.py
```

Pamiętaj, aby w pliku testującym używać pełnych ścieżek importów, na przykład:

```python
from ankiety.models import Person, Team
from ankiety.serializers import PersonSerializer, TeamModelSerializer
```

To powinno w pełni przygotować i przetestować serializery w Twoim projekcie Django. Jeśli masz jeszcze jakieś pytania lub potrzebujesz pomocy, daj znać!