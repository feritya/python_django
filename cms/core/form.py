# cms/forms.py
from django import forms
from .models import Makale

class MakaleForm(forms.ModelForm):
    class Meta:
        model = Makale
        fields = ['baslik', 'icerik']
