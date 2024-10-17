## Zadanie 10

```python
# Poniższy kod został uruchomiony w Django shell
from polls.models import Osoba, Stanowisko

# 1. Wyświetl wszystkie obiekty modelu Osoba
osoby = Osoba.objects.all()
print("Wszystkie obiekty modelu Osoba:")
for osoba in osoby:
    print(osoba)

# Wynik:
# Wszystkie obiekty modelu Osoba:
# Ewa Kowalczyk
# Jan Kowalski
# Jan Kowalski
# Anna Nowak
# Anna Nowak
# Piotr Wiśniewski
# Piotr Wiśniewski

# 2. Wyświetl obiekt modelu Osoba z id = 3
try:
    osoba_z_id_3 = Osoba.objects.get(id=3)
    print(f"Obiekt Osoba z id = 3: {osoba_z_id_3}")
except Osoba.DoesNotExist:
    print("Obiekt o id = 3 nie istnieje")

# Wynik:
# Obiekt Osoba z id = 3: Piotr Wiśniewski

# 3. Wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na literę "K"
osoby_na_k = Osoba.objects.filter(nazwisko__startswith='K')
print("Osoby, których nazwisko zaczyna się na literę 'K':")
for osoba in osoby_na_k:
    print(osoba)

# Wynik:
# Osoby, których nazwisko zaczyna się na literę 'K':
# Ewa Kowalczyk
# Jan Kowalski
# Jan Kowalski

# 4. Wyświetl unikalną listę stanowisk przypisanych do modeli Osoba
unikalne_stanowiska = Stanowisko.objects.filter(osoba__isnull=False).distinct()
print("Unikalna lista stanowisk przypisanych do modeli Osoba:")
for stanowisko in unikalne_stanowiska:
    print(stanowisko)

# Wynik:
# Unikalna lista stanowisk przypisanych do modeli Osoba:
# Manager
# Developer
# Tester
# Manager
# Developer
# Tester

# 5. Wyświetl nazwy stanowisk posortowane alfabetycznie malejąco
sorted_stanowiska = Stanowisko.objects.order_by('-nazwa')
print("Nazwy stanowisk posortowane alfabetycznie malejąco:")
for stanowisko w sorted_stanowiska:
    print(stanowisko.nazwa)

# Wynik:
# Nazwy stanowisk posortowane alfabetycznie malejąco:
# Tester
# Tester
# Manager
# Manager
# Developer
# Developer

# 6. Dodaj nową instancję obiektu klasy Osoba i zapisz w bazie
nowa_osoba = Osoba.objects.create(
    imie="Ewa",
    nazwisko="Kowalczyk",
    plec=Osoba.Plec.KOBIETA,
    stanowisko=Stanowisko.objects.first()
)
print(f"Dodana nowa osoba: {nowa_osoba}")

# Wynik:
# Dodana nowa osoba: Ewa Kowalczyk
'''
```

### Krok 2: Zatwierdzenie pliku w systemie kontroli wersji Git

1. Otwórz terminal wbudowany w PyCharm lub użyj zewnętrznego terminala.
2. Upewnij się, że znajdujesz się w katalogu swojego projektu. Możesz to zrobić poleceniem:
   ```sh
   cd /sciezka/do/twojego/projektu
   ```

3. Dodaj nowo utworzony plik do Git:
   ```sh
   git add lab_3_zadanie_10.md
   ```

4. Zatwierdź zmiany w Git:
   ```sh
   git commit -m "Dodanie pliku lab_3_zadanie_10.md z wynikami zapytań"
   ```

5. Prześlij zmiany do zdalnego repozytorium na gałęzi `lab_3`:
   ```sh
   git push origin lab_3
   ```

### Krok 3: Scal gałąź `lab_3` z `main`

1. Przełącz się na gałąź `main`:
   ```sh
   git checkout main
   ```

2. Wykonaj scalanie z gałęzią `lab_3`:
   ```sh
   git merge lab_3
   ```

3. Jeśli wystąpią konflikty:
   - Otwórz PyCharm.
   - W menu głównym wybierz `VCS` (Version Control System).
   - Wybierz `Git`, a następnie `Resolve Conflicts`.

4. Rozwiąż konflikty (jeśli wystąpią), wybierając odpowiednie zmiany i klikając `Accept`.

5. Po rozwiązaniu konfliktów, zatwierdź zmiany i przekaż je do zdalnego repozytorium:
   ```sh
   git commit -m "Rozwiązanie konfliktów podczas scalania lab_3 z main"
   git push origin main
   ```

Gratulacje! Pomyślnie ukończyłeś zadanie. Czy jest coś, co mogę jeszcze dla Ciebie zrobić?