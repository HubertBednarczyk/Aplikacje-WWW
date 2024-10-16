from django.contrib import admin

from django.contrib import admin
from .models import Team
from .models import Person

admin.site.register(Team)
admin.site.register(Person)