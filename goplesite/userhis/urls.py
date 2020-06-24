from django.urls import path

from . import views

app_name = 'userhis'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<int:usrid>/results/', views.results, name='results')
]