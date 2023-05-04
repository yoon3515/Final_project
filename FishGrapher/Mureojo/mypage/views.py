from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .urls import *
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from mypage.forms import CustomUserChangeForm
from django.contrib import messages
import time
from django.http import HttpResponseServerError, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.exceptions import SuspiciousOperation
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required
def mypage(request):
    return render(request, 'mypage/mypage.html')


@login_required
def modify_pw(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            return HttpResponse("비밀번호 수정이 완료되었습니다. 새로운 비밀번호로 로그인 해주세요.", status=200)

        else:
            print(password_form.errors)
            error_messages = []
            for field, errors in password_form.errors.items():
                for error in errors:
                    error_messages.append(error)
            error_message_all = ', '.join(error_messages)
            if '필수' in error_message_all:
                error_message = '비밀번호를 입력해주세요.'
            elif '기존' in error_message_all:
                error_message = '기존 비밀번호가 일치하지 않습니다.'
            elif '짧습' in error_message_all:
                error_message = '새로운 비밀번호가 너무 짧습니다. 8자~16자의 비밀번호를 입력해주세요.'
            elif '일상' in error_message_all:
                error_message = '새로운 비밀번호가 너무 단순합니다.'
            elif '숫자' in error_message_all:
                error_message = '새로운 비밀번호가 너무 단순합니다.'
            elif '유사' in error_message_all:
                error_message = '새로운 비밀번호가 아이디와 너무 유사합니다.'
            else:
                error_message = '알 수 없는 에러가 발생했습니다.'

            messages.error(request, error_message)
            return redirect('mypage:modify_pw')

    else:
        return render(request, 'mypage/modify_pw.html')

@login_required
def delete_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 아이디와 비밀번호가 일치하는 경우
            logout(request)
            user.delete()
            # return render(request, 'mypage/delete.html')
            return HttpResponse("회원 탈퇴가 완료되었습니다.",status=200)
        else:
            error_message = '아이디와 비밀번호를 확인해주세요'


            messages.error(request, error_message)
            return redirect('mypage:delete_profile')
    else:
        return render(request, 'mypage/delete.html')



@login_required
def edit_profile(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                form = CustomUserChangeForm(request.POST, instance=request.user)
                if  form.is_valid():
                    form.save()
                    messages.success(request, '회원정보 변경 성공')
                    return redirect('mypage:showinfo')
            else:
                error_message = '비밀번호를 확인해주세요'
                messages.error(request, error_message)
                return redirect('mypage:showinfo')

        else:
            form = CustomUserChangeForm(user=user, instance=user)
            context = {
                'form': form,
            }
            return render(request, 'mypage/mypage.html', context)




