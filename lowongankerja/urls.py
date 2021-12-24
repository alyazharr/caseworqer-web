from django.urls import path
from . import views
from .views import jsonMethod

app_name = 'lowongankerja'
urlpatterns = [
    path('lowonganForm', views.lowonganForm, name='lowonganForm'),
    path('json', jsonMethod, name ='json'),
]