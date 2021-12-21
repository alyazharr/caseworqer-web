from django.urls import path

from . import views

app_name = 'profilperusahaan'

urlpatterns = [
    path('formprofilperusahaan', views.lengkapiProfil, name='formprofilperusahaan'),
    path('', views.detailPerusahaan, name='detailperusahaan'),
    path('companiesjson', views.companiesJson, name='companiesjson'),
    path('pelamarjson', views.pelamarJson, name='pelamarjson'),
     path('lowonganjson', views.lowonganJson, name='lowonganjson'),
]