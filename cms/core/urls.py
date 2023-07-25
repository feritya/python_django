from django.urls import path
from .views import  makale_list,makale_ekle

urlpatterns = [
    path('makaleler/', makale_list, name='makale_list'),
    path('makale_ekle/', makale_ekle, name='makale_ekle'), 


]