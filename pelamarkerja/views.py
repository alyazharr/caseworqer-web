from django.shortcuts import redirect,render
from main.models import LowonganKerja,Pelamar
from pelamarkerja.forms import PelamarForm
from django.http.response import HttpResponse
from django.core import serializers 
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


def cariLowongan(request):
    jobList = LowonganKerja.objects.all()
    response = {'jobList': jobList}
    return render(request, 'cariLowongan.html', response)

@csrf_exempt
def lamar(request):
    context = {}
    # create object of form
    try:
        receivedJson = json.loads(request.body)
        print(receivedJson)
        form = PelamarForm(receivedJson)
        form.save()
        web = False
    except:
        form = PelamarForm(request.POST or None)
        web = True

    # check if form data is valid
    if form.is_valid() and request.method == 'POST' and web==True:
        # save the form data to model
        form.save()
        return redirect("../pelamarkerja/carilowongan")
    system = request.POST.get('system', None)
    context['form'] = form
    context['system'] = system
    return render(request, "lamar.html", context)

def jsonMethod(request):
    data = serializers.serialize('json', LowonganKerja.objects.all())
    return HttpResponse(data, content_type="application/json")
