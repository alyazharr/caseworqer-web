from django.urls import path

from . import views
from .views import json

app_name = 'pelamarkerja'

urlpatterns = [
    path('carilowongan', views.cariLowongan, name='carilowongan'),
    path('lamar', views.lamar, name='lamar'),
    path('json', json, name ='json'),
]