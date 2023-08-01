# my_cms_app/views.py
from django.shortcuts import render, get_object_or_404
from .models import Page

def home(request):
    pages = Page.objects.all()
    return render(request, 'home.html', {'pages': pages})

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page_detail.html', {'page': page})
def index(request):
    return render(request, 'index.html')