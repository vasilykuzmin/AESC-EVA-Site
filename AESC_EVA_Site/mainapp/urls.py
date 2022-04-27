from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('wiki', views.wiki, name='wiki'),
    path('posters', views.posters, name='posters'),
    path('rock', views.rock, name='rock'),
    path('authors', views.authors, name='authors'),
    path('rickroll', views.rickroll, name='rickroll'),

]