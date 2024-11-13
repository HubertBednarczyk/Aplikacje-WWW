from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    SHIRT_SIZES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    MONTHS = models.IntegerChoices('Month',
                                   'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

    name = models.CharField(max_length=100)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    miesiac_dodania = models.IntegerField(choices=MONTHS.choices)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    data_dodania = models.DateTimeField(auto_now_add=True)
    wlasciciel = models.ForeignKey(User, on_delete=models.CASCADE,
                                   default=1)  # Wartość domyślna jako ID utworzonego użytkownika

    def __str__(self):
        return self.name
