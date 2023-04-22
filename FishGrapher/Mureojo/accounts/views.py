from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import User
from .forms import UserForm

# Create your views here.


def CustomSignup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = User.objects.create(username=username, email=email, password=raw_password)
            return redirect('accounts:login')

    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})


def CustomLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user using MongoDB
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login user
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'accounts/login.html')


def CustomLogout(request):
    logout(request)
    return redirect('home')
