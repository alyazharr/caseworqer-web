from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import  Tipskarier
from .forms import EditForm, TipsForm
from django.urls import reverse_lazy

# Create your views here.
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

def add_artikel(request):
    context = {}
    form = TipsForm(request.POST or None, request.FILES or None)
        
    if form.is_valid():

        form.save()
        return redirect('tipskarier:tipskarier')
    context['form']= form
    return render(request, "tipskarier_form.html", context) 

class UpdateArtikel(UpdateView):
    model = Tipskarier
    form_class = EditForm
    template_name = 'tipskarier_update.html'

   
class DeleteArtikel(DeleteView):
    model = Tipskarier
    template_name = 'tipskarier_hapus.html'
    success_url = reverse_lazy('tipskarier:tipskarier')

