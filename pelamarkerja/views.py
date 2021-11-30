from django.shortcuts import redirect,render
from main.models import LowonganKerja,Pelamar
from pelamarkerja.forms import PelamarForm
from django.http.response import HttpResponse
from django.core import serializers 
# Create your views here.


def cariLowongan(request):
    jobList = LowonganKerja.objects.all()
    response = {'jobList': jobList}
    return render(request, 'cariLowongan.html', response)

def lamar(request):
    context = {}
    # create object of form
    form = PelamarForm(request.POST or None)

    # check if form data is valid
    if form.is_valid() and request.method == 'POST':
        # save the form data to model
        form.save()
        return redirect("../pelamarkerja/carilowongan")
    system = request.POST.get('system', None)
    context['form'] = form
    context['system'] = system
    return render(request, "lamar.html", context)

def json(request):
    data = serializers.serialize('json', LowonganKerja.objects.all())
    return HttpResponse(data, content_type="application/json")
