# my_cms_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page/index/', views.index, name='index'),
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),
    
]
