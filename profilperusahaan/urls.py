from django.urls import path

from . import views

app_name = 'profilperusahaan'

urlpatterns = [
    path('formprofilperusahaan', views.lengkapiProfil, name='formprofilperusahaan'),
    path('', views.detailPerusahaan, name='detailperusahaan')
]