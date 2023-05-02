from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import View
from .decorators import logout_message_required
from .forms import RecoverIdForm, UserForm
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
    form = RecoverIdForm

    def get(self, request):
        if request.method=='GET':
            form = self.recover_id(None)
        return render(request, self.template_name, { 'form':form, })


def ajax_find_id_view(request):
    email = request.POST.get('email')
    result_id = User.objects.get(email=email)

    return HttpResponse(json.dumps({"result_id": result_id.user_id}, cls=DjangoJSONEncoder), content_type = "application/json")
