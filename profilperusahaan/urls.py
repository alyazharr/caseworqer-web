from django.urls import path

from . import views

app_name = 'profilperusahaan'

urlpatterns = [
    path('formProfilPerusahaan', views.lengkapiProfil, name='formProfilPerusahaan'),
    path('', views.detailPerusahaan, name='detailperusahaan')
]