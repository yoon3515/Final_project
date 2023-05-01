from django import forms
from .models import MyFish

class MyFishForm(forms.ModelForm):
    class Meta:
        model = MyFish
        fields = ['name', 'image']
