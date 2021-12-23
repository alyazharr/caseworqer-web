from django.urls import path

# from . import view
from .views import UpdateArtikel, tipskarier, ArticleDetail,add_artikel,UpdateArtikel,DeleteArtikel, search_results,editmode,json

app_name = 'tipskarier'

urlpatterns = [
    path('', tipskarier.as_view(), name='tipskarier'),
    path('article/<int:pk>/',ArticleDetail.as_view(),name='detail'),
    path('add/', add_artikel, name='add_artikel'),
    path('article/edit/<int:pk>/',UpdateArtikel.as_view(),name='update_artikel'),
    path('article/<int:pk>/remove',DeleteArtikel.as_view(),name='delete_artikel'),
    path('search/', search_results, name='search'),
    path('editmode/',editmode,name='editmode'),
    path('json/',json, name = 'json'),
]