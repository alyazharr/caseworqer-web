from django.db.models.expressions import Value
from django.shortcuts import render,redirect
from company_review.models import perusahaanKomen
from main.models import LowonganKerja
from company_review.forms import reviewForm
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse,HttpResponse
from django.core import serializers 
from django.views.decorators.csrf import csrf_exempt
import json as djson
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

@csrf_exempt
def read_job(request, id_job):
    response = {}
    job = LowonganKerja.objects.get(id=id_job)
    comment = perusahaanKomen.objects.filter(pekerjaan=job)
    
    avg = 0
    for komen in comment:
        avg += komen.value   
    if len(comment) == 0:
        avg = int(avg)
    else:
        avg = (avg/len(comment))

    # try:
    #     get_json = json.loads(request.body)
    #     print(get_json)
    #     addReview = reviewForm(get_json)

    #     if addReview.is_valid():
    #         addReview_new = addReview.save(commit=False)
    #         addReview_new.pekerjaan_id = get_json['pekerjaan']
    #     addReview.save()
    #     web = False
    
    # except:
    #     web = True
    #     if request.user.is_authenticated:
    #         penulis  = request.user.get_username()
        
    #     addReview = reviewForm(request.POST or None)
    #     value = addReview.save(job, request.user)
    #     value.value = int(request.POST['rate'][0])

    #     response['pekerjaan'] = job
    #     response['penulis'] = penulis
    #     response['value'] = value.value
    #     response['description'] = addReview
        
    if request.method == 'POST' and request.is_ajax and request.user.is_authenticated and web==True:
        post = reviewForm(request.POST)
        if post.is_valid():
            komentar = post.save(job, request.user)
            print(request.POST)
            komentar.value = int(request.POST['rate'][0])
            komentar.save()
            return JsonResponse({ 'pesan' : 'Sukses'})
    if request.user.is_authenticated:
        komentar = perusahaanKomen.objects.filter(pekerjaan=job).filter(penulis=request.user)
    else:
        komentar =  perusahaanKomen.objects.all()
    if komentar:
        sudah_komen = True
    else:
        sudah_komen = False
    return render(request, 'job_company.html', {
		'job' : job, 'sudah_komen' : sudah_komen, 'comment' : comment,
        'avg' : avg,
	})

@csrf_exempt
def postMethod(request, id_job):
    # taken and edited from https://stackoverflow.com/questions/40059654/python-convert-a-bytes-array-into-json-format/40060181
    if (request.method == 'POST'):
        data = djson.loads(request.body)
        jobs = data['pekerjaan']
        penulis = data['penulis']
        value = data['value']
        description = data['description']

        job = LowonganKerja.objects.get(id=id_job)
        data_baru = perusahaanKomen.objects.filter(pekerjaan=job)
        target = None
        for i in data_baru:
            if i == perusahaanKomen.objects.filter(pekerjaan=job):
                target = i
                break
        
        target.jobs = jobs
        target.penulis = penulis
        target.value = value
        target.description = description

        target.save()

        return ({'status':200})


def json_joblist(request):
    data_joblist = serializers.serialize('json', LowonganKerja.objects.all())
    return HttpResponse(data_joblist, content_type="apllication/json")

def json_jobrate(request):
    data_jobreview = serializers.serialize('json', perusahaanKomen.objects.all(), 
    use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(data_jobreview, content_type="application/json")