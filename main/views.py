from django.shortcuts import render
import requests

def home(request):
    response = requests.get('https://api.kawalcorona.com/indonesia')
    coronaData = response.json()
    return render(request, 'home.html', {
        'name': coronaData[0]['name'],
        'positif': coronaData[0]['positif'],
        'sembuh': coronaData[0]['sembuh'],
        'meninggal': coronaData[0]['meninggal'],
    })
