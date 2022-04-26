from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('posters', views.posters, name='posters'),
    path('rickroll', views.rickroll, name='rickroll'),

]