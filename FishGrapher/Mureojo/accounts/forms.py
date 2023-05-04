from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm

# Create your forms here.

class UserForm(UserCreationForm):
    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class RecoverIdForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': '  이메일 주소를 입력하세요.'}))

    class Meta:
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(RecoverIdForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_email'
        })


class RecoverPwForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '  아이디를 입력하세요.'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': '  이메일 주소를 입력하세요.'}))

    class Meta:
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(RecoverPwForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_username'
        })
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_email'
        })


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control', 
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })