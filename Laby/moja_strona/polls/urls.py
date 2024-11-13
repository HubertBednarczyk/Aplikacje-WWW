from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.person_list, name='person_list'),
    path('persons/<int:pk>/', views.person_detail, name='person_detail'),
    path('stanowisko/<int:team_id>/members/', views.team_members, name='team_members'),
]
