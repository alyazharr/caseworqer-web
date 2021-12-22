from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.core import serializers
from django.http.response import HttpResponse
from profilperusahaan.models import ProfilPerusahaan
from main.models import LowonganKerja, Pelamar
from profilperusahaan.forms import ProfilPerusahaanForm
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def detailPerusahaan(request):
    theCompany = ProfilPerusahaan.objects.all()
    pelamarAll = Pelamar.objects.all()
    lowonganAll = LowonganKerja.objects.all()
    response = {'theCompany': theCompany, 'pelamarAll' : pelamarAll, 'lowonganAll' : lowonganAll}
    return render(request, 'detailPerusahaan.html', response)

@csrf_exempt
def lengkapiProfil(request):
    context = {}

    # menciptakan object form
    try:
        dataReceived = json.loads(request.body)
        print(dataReceived)
        form = ProfilPerusahaanForm(dataReceived)
        form.save()
        fromWeb = False
    except:    
        form = ProfilPerusahaanForm(request.POST or None)
        fromWeb = True

    # memeriksa apakah data form valid, metode request adalah POST, dan form berasal dari web
    if form.is_valid() and request.method == 'POST' and fromWeb == True:
        # menyimpan data form ke model
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