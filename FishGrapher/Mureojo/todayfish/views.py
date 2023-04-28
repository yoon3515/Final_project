from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import MyFishForm

# Create your views here.

def save_image(request):
    if request.method == 'POST':
        form = MyFishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({ 'success': True })
    else:
        form = MyFishForm()
    return render(request, 'save_image.html', {'form': form})
