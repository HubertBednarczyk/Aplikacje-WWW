from django.db import models
from django.utils import timezone


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

    MONTHS = models.TextChoices('MONTHS',
                                'January February March April May June July August September October November December')

    name = models.CharField(max_length=100)
    shirt_size = models.CharField(max_length=3, choices=SHIRT_SIZES, default='S')
    miesiac_dodania = models.CharField(max_length=9, choices=MONTHS.choices, default='January')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    data_dodania = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
