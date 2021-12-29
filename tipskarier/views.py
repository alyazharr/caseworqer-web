
from json.decoder import JSONDecodeError
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import  Tipskarier
from .forms import EditForm, TipsForm
from django.urls import reverse_lazy
from django.core import serializers 
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create  views here.
def search_results(request):
    if request.is_ajax():
        res = None
        artikels= request.POST.get('artikel')
        qs = Tipskarier.objects.filter(Title__icontains = artikels)
        if len(qs)> 0 and len(artikels)>0:
            data = []
            for pos in qs:
                item = {
                    'pk': pos.pk,
                    'Title' : pos.Title,
                    'Cover' : str(pos.Cover.url),
                    'Summary':pos.Summary,
                }
                data.append(item)
            res = data
        else:
            res = 'No article found ...'
        

        return JsonResponse({'data': res})

    return JsonResponse({})

class tipskarier(ListView):
    model = Tipskarier
    template_name = 'tipskarier.html'
    ordering = ['-id']

def editmode(request):
    artikels = Tipskarier.objects.all().values()
    response = {'artikels' : artikels}
    return render(request, "tipskarier_list.html", response)

class ArticleDetail (DetailView):
    model = Tipskarier
    template_name = 'tipskarier_detail.html'


class UpdateArtikel(UpdateView):
    model = Tipskarier
    form_class = EditForm
    template_name = 'tipskarier_update.html'

   
class DeleteArtikel(DeleteView):
    model = Tipskarier
    template_name = 'tipskarier_hapus.html'
    success_url = reverse_lazy('tipskarier:editmode')



@csrf_exempt
def add_artikel(request):
    context = {}
    try:
        receivedJson1 = json.loads(request.body)
        print(receivedJson1)
        form = TipsForm(receivedJson1)
        form.save()
        jsonweb = False
       
    except :
       # print(e)
      
        print("gagal membuat objek mobile")
       
        form = TipsForm(request.POST or None,request.FILES or None)
        jsonweb = True

    #if form.is_valid():
    if form.is_valid() and request.method == 'POST' and jsonweb==True:
        form.save()
        return redirect('tipskarier:tipskarier')
    context['form']= form
    return render(request, "tipskarier_form.html", context) 

def jsonmethod(request):
    data = serializers.serialize('json', Tipskarier.objects.all())
    return HttpResponse(data, content_type="application/json")