from django.http import response
from django.shortcuts import render,redirect
from company_review.models import perusahaanKomen
from main.models import LowonganKerja
from company_review.forms import reviewForm
# Create your views here.

def cardStar(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.get_username()
    if request.POST and 'search-bar' in request.POST:
        listJob = LowonganKerja.objects.filter(jobs__icontains = request.POST['search-bar'])
    else:
        listJob = LowonganKerja.objects.all()
    response = {'author':username, 'listJob' : listJob}
    return render(request, 'company-review.html', response)

def read_job(request, id_job):
    job = LowonganKerja.objects.get(id=id_job)
    comment = perusahaanKomen.objects.filter(pekerjaan=job)
    avg = 0
    for komen in comment:
        avg+=komen.value
    avg= int(avg/len(comment))
    if request.method == 'POST':
        post = reviewForm(request.POST)
        if post.is_valid():
            komentar = post.save(job, request.user)
            print(request.POST)
            komentar.value = int(request.POST['rate'][0])
            komentar.save()
            return redirect('/company_review/')
    komentar = perusahaanKomen.objects.filter(pekerjaan=job).filter(penulis=request.user)
    if komentar:
        sudah_komen = True
    else:
        sudah_komen = False
    return render(request, 'job_company.html', {
		'job' : job, 'sudah_komen' : sudah_komen, 'comment' : comment,
        'avg' : avg,
	})