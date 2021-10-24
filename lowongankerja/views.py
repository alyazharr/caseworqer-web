from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from main.models import LowonganKerja
from .forms import PembukaLowonganForm
import requests

# Create your views here.
#def index(request):
#    lowongan = LowonganKerja.objects.all()
#    response = {'lowongan': lowongan}
#    return render(request, 'indexlowongan.html', response)

def lowonganForm(request):
    if request.method == 'POST':
        form = PembukaLowonganForm(request.POST)
        if form.is_valid():
            print("berhasil")
            form.save()
            return redirect('/bukalowongan')
        
    else:
        form = PembukaLowonganForm()

    return render(request, 'bukaLowongan.html', {'form': form})