from django.shortcuts import render
import requests
from django.http.response import HttpResponse
from django.core import serializers 
import json
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    response = requests.get('https://api.kawalcorona.com/indonesia')
    coronaData = response.json()
    return render(request, 'home.html', {
        'name': coronaData[0]['name'],
        'positif': coronaData[0]['positif'],
        'sembuh': coronaData[0]['sembuh'],
        'meninggal': coronaData[0]['meninggal'],
    })
    # return render(request, 'home.html')

@csrf_exempt
def login_flutter(request):
# username = request.get("username")
# password = request.get("password")
    print(request.method)
# print(request.GET)
    print(request.body)
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    print(f"{username} n {password}")
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
        print("Hore")
        return JsonResponse({"status": "logged in", "username": username})
    else:
        print("Sad")
    return JsonResponse({"out": "no"})