from rest_framework import serializers
from .models import Person, Team
from django.utils import timezone


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    shirt_size = serializers.ChoiceField(choices=Person.SHIRT_SIZES, default=Person.SHIRT_SIZES[0][0])
    miesiac_dodania = serializers.ChoiceField(choices=Person.MONTHS.choices, default=Person.MONTHS.choices[0][0])
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    data_dodania = serializers.DateTimeField(default=timezone.now)  # Usuń required=True

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Nazwa może zawierać tylko litery!")
        return value

    def validate_data_dodania(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("Data dodania nie może być z przyszłości!")
        return value

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.shirt_size = validated_data.get('shirt_size', instance.shirt_size)
        instance.miesiac_dodania = validated_data.get('miesiac_dodania', instance.miesiac_dodania)
        instance.team = validated_data.get('team', instance.team)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.save()
        return instance


class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']
        read_only_fields = ['id']
