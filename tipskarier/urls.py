from django.urls import path

# from . import views
from .views import UpdateArtikel, tipskarier, ArticleDetail,add_artikel,UpdateArtikel,DeleteArtikel

app_name = 'tipskarier'

urlpatterns = [
    path('', tipskarier.as_view(), name='tipskarier'),
    path('article/<int:pk>/',ArticleDetail.as_view(),name='detail'),
    path('add/', add_artikel, name='add_artikel'),
    path('article/edit/<int:pk>/',UpdateArtikel.as_view(),name='update_artikel'),
    path('article/<int:pk>/remove',DeleteArtikel.as_view(),name='delete_artikel'),
   
]