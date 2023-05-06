from django.shortcuts import redirect
from django.contrib import messages

# Create your decorators here.

# 로그인 여부 확인
def logout_message_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "접속 중인 사용자입니다.")
            return redirect('home')
        return function(request, *args, **kwargs)
    return wrap
