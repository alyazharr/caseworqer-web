from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

# Create your views here.
from django.http import HttpResponseRedirect
from django.http import response
from django.shortcuts import render,redirect
from django.views import View

from .models import  Tipskarier
from .forms import TipsForm
from django.urls import reverse_lazy

class tipskarier(ListView):
    model = Tipskarier
    template_name = 'tipskarier.html'
    ordering = ['-id']

class ArticleDetail (DetailView):
    model = Tipskarier
    template_name = 'tipskarier_detail.html'


# def tipskarier(request): # ini buat nulis isi boxnya apa aja
#     artikels = Tipskarier.objects.all().values()
#     response = {'artikels': artikels}
#     return render(request, 'tipskarier.html', response)


def add_artikel(request):
    context = {}
    form = TipsForm(request.POST or None, request.FILES or None)
        
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect('tipskarier:tipskarier')
    context['form']= form
    return render(request, "tipskarier_form.html", context) 

class UpdateArtikel(UpdateView):
    model = Tipskarier
    template_name = 'tipskarier_update.html'
    fields = ['Title', 'Article', 'Cover']
   
class DeleteArtikel(DeleteView):
    model = Tipskarier
    template_name = 'tipskarier_hapus.html'
    success_url = reverse_lazy('tipskarier:tipskarier')
    