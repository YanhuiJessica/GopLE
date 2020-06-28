from django.urls import path

from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<str:keyword>/<str:genre>/results/', views.results, name='results'),
    path('<str:keyword>/results', views.key_results, name='key_results'),
    path('<str:genre>/results', views.style_results, name='style_results')
]