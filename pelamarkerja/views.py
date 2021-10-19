from django.shortcuts import render

# Create your views here.
def cariLowongan(request):
    return render(request, 'cariLowongan.html')