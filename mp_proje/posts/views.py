from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

class AnaSayfaView(ListView):
    model =Post
    template_name ='home.html'
    contex_object_name ='all_posts_list'