from django.urls import path

from . import views

app_name = 'pelamarkerja'

urlpatterns = [
    path('carilowongan', views.cariLowongan, name='carilowongan'),
]