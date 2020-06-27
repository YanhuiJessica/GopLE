from django.urls import path

from . import views

app_name = 'recommend'
urlpatterns = [
    path('', views.index, name='index'),
    path('change_gender/', views.change_gender, name='change_gender')
]