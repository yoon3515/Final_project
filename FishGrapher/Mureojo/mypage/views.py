from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from mypage.forms import PasswordChangeForm


# Create your views here.
def mypage(request):
    return render(request, 'mypage/mypage.html')



# @login_required
# def edit_profile(request):
#     user = request.user
#     if request.method == 'POST':
#         user_form = CustomUserChangeForm(request.POST, user=user, instance=user)
#         password_form = PasswordChangeForm(request.user, request.POST)
#         if user_form.is_valid() and password_form.is_valid():
#             user_form.save()
#             password_form.save()
#             update_session_auth_hash(request, request.user)
#             messages.success(request, '프로필이 수정되었습니다.')
#             return redirect('mypage:index')
#     else:
#         user_form = CustomUserChangeForm(user=user, instance=user)
#         password_form = PasswordChangeForm(request.user)
#     context = {
#         'user_form': user_form,
#         'password_form': password_form,
#     }
#     return render(request, 'mypage/mypage.html', context)




# @login_required
# def edit_profile(request):
#     user = request.user
#     if request.method == 'POST':
#         password_form = CustomPasswordChangeForm(request.user, request.POST)
#         if password_form.is_valid():
#             new_password = password_form.cleaned_data['new_password1']
#             user.set_password(new_password)
#             user.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, '비밀번호가 변경되었습니다.')
#             return redirect('mypage:index')
#     else:
#         password_form = CustomPasswordChangeForm(request.user)
#     context = {
#         'password_form': password_form,
#     }
#     return render(request, 'mypage/mypage.html', context)


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, '비밀번호가 수정되었습니다.')
            return redirect('mypage:index')
        else:
            print(password_form.errors)
    else:
        password_form = PasswordChangeForm(request.user)
    context = {
        'password_form': password_form,
    }
    return HttpResponse(password_form.errors)






# @login_required
# def edit_profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, request.user)
#             messages.success(request, '프로필이 수정되었습니다.')
#             return redirect('mypage:index')
#     else:
#         form = CustomUserChangeForm(instance=request.user)
#     return render(request, 'mypage/mypage.html', {'form': form})


# def password(request):
#     if request.method == "POST":
#         password_change_form = PasswordChangeForm(request.user, request.POST)
#
#         if password_change_form.is_valid():
#             user = password_change_form.save()
#             update_session_auth_hash(request, user)
#
#     else:
#         password_change_form = PasswordChangeForm(request.user)
#         context = {
#             'password_change_form': password_change_form
#         }
#
#         return render(request, 'password.html', context)


