from django.shortcuts import render
from main.models import LowonganKerja
from pelamarkerja.forms import PelamarForm
# Create your views here.

def cardStar(request):
    listJob = LowonganKerja.objects.all()
    response = {'listJob' : listJob}
    return render(request, 'company-review.html', response)
