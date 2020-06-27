from django.urls import path

from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('results/', views.results, name='results'),
    path('tops/',views.tops,name='tops')
]