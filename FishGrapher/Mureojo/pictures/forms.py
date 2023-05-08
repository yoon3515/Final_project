from django import forms
from .models import PictureSave

class PictureSaveForm(forms.ModelForm):
    class Meta:
        model = PictureSave
        fields = ['name', 'image']
