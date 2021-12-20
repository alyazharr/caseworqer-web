from django.urls import path

from . import views
from .views import jsonMethod

app_name = 'pelamarkerja'

urlpatterns = [
    path('carilowongan', views.cariLowongan, name='carilowongan'),
    path('lamar', views.lamar, name='lamar'),
    path('json', jsonMethod, name ='json'),
]