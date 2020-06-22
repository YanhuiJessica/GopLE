from django.urls import path

from . import views

app_name = 'userhis'
urlpatterns = [
    path('', views.search, name='search')
]