from django import forms
from .models import *
class TalabaForm(forms.Form):
    ism=forms.CharField(max_length=255)
    guruh=forms.CharField(max_length=255)
    kurs=forms.IntegerField(min_value=1, max_value=4)
    kitob_soni=forms.IntegerField()


class KitobForm(forms.ModelForm):
    class Meta:
        model=Kitob
        fields=('__all__')