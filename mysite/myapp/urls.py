from unicodedata import name
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('market', views.v1, name='mart'),
    path("lol", views.lol, name="lol"),
    path("add", views.add, name="add"),
]