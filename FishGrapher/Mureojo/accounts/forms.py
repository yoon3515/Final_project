from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class RecoverIdForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(RecoverIdForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_email'
        })