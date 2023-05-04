# forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')
    #
    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super().__init__(*args, **kwargs)
    #     if user:
    #         self.fields['username'].initial = user.username
    #         self.fields['email'].initial = user.email


# class CustomPasswordChangeForm(PasswordChangeForm):
#     def __init__(self, user, *args, **kwargs):
#         super(CustomPasswordChangeForm, self).__init__(user, *args, **kwargs)
#         # 'old_password' 필드 제거
#         self.fields.pop('old_password')
#
#     def clean(self):
#         cleaned_data = super(CustomPasswordChangeForm, self).clean()
#         # 'old_password' 필드 검증 생략
#         return cleaned_data



# class PasswordChangeForm(forms.Form):
#     old_password = forms.CharField(
#         label='기존 비밀번호', widget=forms.PasswordInput(attrs={'class': 'inputTypeText'}))
#     new_password1 = forms.CharField(
#         label='새로운 비밀번호', widget=forms.PasswordInput(attrs={'class': 'inputTypeText'}))
#     new_password2 = forms.CharField(
#         label='새로운 비밀번호 확인', widget=forms.PasswordInput(attrs={'class': 'inputTypeText'}))
#
#     def clean(self):
#         cleaned_data = super().clean()
#         old_password = cleaned_data.get('old_password')
#         new_password1 = cleaned_data.get('new_password1')
#         new_password2 = cleaned_data.get('new_password2')
#         if old_password and new_password1 and new_password2:
#             if not self.user.check_password(old_password):
#                 raise forms.ValidationError('기존 비밀번호가 일치하지 않습니다.')
#             if new_password1 != new_password2:
#                 raise forms.ValidationError('새로운 비밀번호가 일치하지 않습니다.')
#         return cleaned_data
