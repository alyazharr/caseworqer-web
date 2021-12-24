from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from main.models import LowonganKerja
from .forms import PembukaLowonganForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# Create your views here.
#def index(request):
#    lowongan = LowonganKerja.objects.all()
#    response = {'lowongan': lowongan}
#    return render(request, 'indexlowongan.html', response)

@csrf_exempt
def lowonganForm(request):
    context = {}
    # object form
    try:
        recJson = json.loads(request.body)
        print(recJson)
        form = PembukaLowonganForm(recJson)
        form.save()
        web = False
    except:
        form = PembukaLowonganForm(request.POST or None)
        web = True

    if request.method == 'POST' and web == True:
        form = PembukaLowonganForm(request.POST)
        if form.is_valid():
            #print("berhasil")
            form.save()
            return redirect('../lowongankerja/lowonganForm')
        
    else:
        form = PembukaLowonganForm()

    system = request.POST.get('system', None)
    context['form'] = form
    context['system'] = system

    return render(request, 'bukaLowongan.html', {'form': form})

def jsonMethod(request):
    data = serializers.serialize('json', LowonganKerja.objects.all())
    return HttpResponse(data, content_type="application/json")