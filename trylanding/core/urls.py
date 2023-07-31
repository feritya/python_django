from django.urls import path

from .views import home, navbar_detail

urlpatterns = [
    path("", home, name="home"),
     path('navbar/<int:navbar_id>/', navbar_detail, name='navbar_detail'),
]