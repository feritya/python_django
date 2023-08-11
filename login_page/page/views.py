from django.shortcuts import render

# Create your views here.
def starter(request):
    return render(request, 'partias/home.html')
def home(request):
    return render(request, 'partias/home.html')
