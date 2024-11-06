from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
    path('persons/search/<str:query>/', views.person_search),
    path('teams/', views.team_list),
    path('teams/<int:pk>/', views.team_detail),
]
