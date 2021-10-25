from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import ProfilPerusahaan
from .forms import ProfilPerusahaanForm

# Create your views here.

def detailPerusahaan(request):
    theCompany = ProfilPerusahaan.objects.all()
    response = {'theCompany': theCompany}
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
        return HttpResponseRedirect('/profilperusahaan') # redirect ke detail perusahaan page, detail perusahaan jadi ada
    context['form'] = form
    return render(request, "formProfilPerusahaan.html", context)