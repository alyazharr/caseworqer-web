from django.urls import path
from .views import *

app_name = 'company_review'

urlpatterns = [
    path('',cardStar, name='forum-post'),
    path('job/<str:id_job>', read_job, name='read_job'),
    path('json-joblist', json_joblist, name='json-joblist'),
    path('json-jobrate', json_jobrate, name='json-jobrate')
]