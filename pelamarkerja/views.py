from django.shortcuts import render
from main.models import LowonganKerja
# Create your views here.


def cariLowongan(request):
    jobList = LowonganKerja.objects.all()
    response = {'jobList': jobList}
    return render(request, 'cariLowongan.html', response)
