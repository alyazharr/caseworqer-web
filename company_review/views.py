from django.http import response
from django.shortcuts import render,redirect
from main.models import LowonganKerja
from company_review.forms import reviewForm
# Create your views here.

def cardStar(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.get_username()
    listJob = LowonganKerja.objects.all()
    response = {'author':username, 'listJob' : listJob}
    return render(request, 'company-review.html', response)

def reviewForms(request):
    reviewAddForm = reviewForm
    response = {'addReview':reviewAddForm}
    if request.method == 'POST':
        post = reviewForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('/company_review')
        return render(request, 'company_review.html',response)