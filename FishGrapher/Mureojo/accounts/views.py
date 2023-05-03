from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.generic import View
from .decorators import logout_message_required
from .forms import CustomSetPasswordForm, RecoverIdForm, RecoverPwForm, UserForm
from .helper import email_auth_num, send_mail
from .models import AuthKey
import json

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})


@method_decorator(logout_message_required, name='dispatch')
class RecoverIdView(View):
    template_name = 'accounts/recover_id.html'
    recover_id = RecoverIdForm

    def get(self, request):
        if request.method=='GET':
            form_id = self.recover_id(None)
        return render(request, self.template_name, { 'form_id':form_id, })


def ajax_find_id_view(request):
    email = request.POST.get('email')
    result_id = User.objects.get(email=email)

    return HttpResponse(json.dumps({"result_id": result_id.username}, cls=DjangoJSONEncoder), content_type = "application/json")


@method_decorator(logout_message_required, name='dispatch')
class RecoverPwView(View):
    template_name = 'accounts/recover_pw.html'
    recover_pw = RecoverPwForm

    def get(self, request):
        if request.method=='GET':
            form_pw = self.recover_pw(None)
            return render(request, self.template_name, { 'form_pw':form_pw, })


def ajax_find_pw_view(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    result_pw = User.objects.get(username=username, email=email)

    if result_pw:
        auth_num = email_auth_num()
        code = AuthKey(user=result_pw, auth=auth_num)
        code.save()

        send_mail(
            '[물어조 FISHING] 비밀번호 찾기 인증메일입니다.',
            [email],
            html=render_to_string('accounts/recover_email.html', {
                'auth_num': auth_num,
            }),
        )
    return HttpResponse(json.dumps({"result": result_pw.username}, cls=DjangoJSONEncoder), content_type = "application/json")


def auth_confirm_view(request):
    username = request.POST.get('username')
    input_auth_num = request.POST.get('input_auth_num')
    user = User.objects.get(username=username)
    code = AuthKey.objects.get(user_id=user.id, auth=input_auth_num)
    request.session['auth'] = user.username
    
    return HttpResponse(json.dumps({"result": user.username}, cls=DjangoJSONEncoder), content_type = "application/json")


@logout_message_required
def auth_pw_reset_view(request):
    if request.method == 'GET':
        if not request.session.get('auth', False):
            raise PermissionDenied

    if request.method == 'POST':
        session_user = request.session['auth']
        current_user = User.objects.get(username=session_user)
        login(request, current_user)

        reset_password_form = CustomSetPasswordForm(request.user, request.POST)
        
        if reset_password_form.is_valid():
            user = reset_password_form.save()
            messages.success(request, "비밀번호 변경 완료! 변경된 비밀번호로 로그인하세요.")
            logout(request)
            return redirect('accounts:login')
        else:
            logout(request)
            request.session['auth'] = session_user
    else:
        reset_password_form = CustomSetPasswordForm(request.user)

    return render(request, 'accounts/password_reset.html', {'form':reset_password_form})