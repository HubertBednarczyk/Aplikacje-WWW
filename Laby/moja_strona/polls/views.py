from contextvars import Token

from django.http import HttpResponse
from rest_framework.authtoken.admin import User

from .models import Person, Team
from .serializers import PersonSerializer, TeamModelSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Nowa funkcja obsługująca główną stronę polls/
def polls_home(request):
    return HttpResponse(
        "<h1>Witamy w aplikacji Polls!</h1><p>Dostępne ścieżki:</p><ul><li><a href='persons/'>Persons</a></li><li><a href='teams/'>Teams</a></li></ul>")


# Funkcja generująca tokeny dla istniejących użytkowników
def create_tokens_for_users():
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def person_list(request):
    if request.method == 'GET':
        persons = Person.objects.filter(wlasciciel=request.user)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(wlasciciel=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk, wlasciciel=request.user)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def team_members(request, team_id):
    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    members = Person.objects.filter(team=team, wlasciciel=request.user)
    serializer = PersonSerializer(members, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def person_search(request, query):
    persons = Person.objects.filter(name__icontains=query)
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def team_list(request):
    teams = Team.objects.all()
    serializer = TeamModelSerializer(teams, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def team_detail(request, pk):
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TeamModelSerializer(team)
    return Response(serializer.data)
