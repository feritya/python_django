from django.shortcuts import render
from .models import Navbar, Slider


# Create your views here.
def home (request):
    navbars = Navbar.objects.all()
    sliders = Slider.objects.all()
    context = {
        'navbars': navbars,
        'sliders': sliders,
    }
    return render(request, 'home.html', {'sliders': sliders, 'navbars': navbars})

def navbar_detail(request, navbar_id):
    navbar = Navbar.objects.get(id=navbar_id)
    return render(request, 'navbar_detail.html', {'navbar': navbar})