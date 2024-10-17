from django.contrib import admin

from django.contrib import admin
from .models import Team, Person, Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ('data_dodania',)
    list_display = ('imie', 'nazwisko', 'plec', 'get_stanowisko', 'data_dodania')
    list_filter = ('stanowisko', 'data_dodania')

    @admin.display(description='Stanowisko (id)')
    def get_stanowisko(self, obj):
        return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"


class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = ('nazwa',)

admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)