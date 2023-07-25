
from django.shortcuts import render,redirect
from .models import Makale
from .form import MakaleForm

def makale_ekle(request):
    if request.method == 'POST':
        form = MakaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('makale_ekle')
    else:
        form = MakaleForm()
    return render(request, 'makale_ekle.html', {'form': form})

def makale_list(request):
    makaleler = Makale.objects.all()
    return render(request, 'makale_list.html', {'makaleler': makaleler})
