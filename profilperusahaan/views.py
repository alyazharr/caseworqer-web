from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.core import serializers
from django.http.response import HttpResponse
from profilperusahaan.models import ProfilPerusahaan
from main.models import LowonganKerja, Pelamar
from profilperusahaan.forms import ProfilPerusahaanForm

# Create your views here.

def detailPerusahaan(request):
    theCompany = ProfilPerusahaan.objects.all()
    pelamarAll = Pelamar.objects.all()
    lowonganAll = LowonganKerja.objects.all()
    response = {'theCompany': theCompany, 'pelamarAll' : pelamarAll, 'lowonganAll' : lowonganAll}
    return render(request, 'detailPerusahaan.html', response)

def lengkapiProfil(request):
    context = {}

    # menciptakan object form
    form = ProfilPerusahaanForm(request.POST or None)

    # memeriksa apakah data form valid dan metode request adalah POST
    if form.is_valid() and request.method == 'POST':
        # menyimpan data form ke model
        print("berhasil")
        form.save()
        return redirect('../profilperusahaan') # redirect ke detail perusahaan page, detail perusahaan jadi ada/bertambah
    context['form'] = form
    return render(request, "formProfilPerusahaan.html", context)

def companiesJson(request):
    companies = ProfilPerusahaan.objects.all() # Load ProfilPerusahaan model in json method
    data = serializers.serialize('json', companies)
    return HttpResponse(data, content_type="application/json") 

def pelamarJson(request):
    pelamars = Pelamar.objects.all() # Load Pelamar model in json method
    data = serializers.serialize('json', pelamars)
    return HttpResponse(data, content_type="application/json")

def lowonganJson(request):
    lowongans = LowonganKerja.objects.all() # Load LowonganKerja model in json method
    data = serializers.serialize('json', lowongans)
    return HttpResponse(data, content_type="application/json")     