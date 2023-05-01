from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import PictureSaveForm

# Create your views here.

def save_image(request):
    if request.method == 'POST':
        form = PictureSaveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({ 'success': True })
    else:
        form = PictureSaveForm()
    return render(request, 'save_image.html', {'form': form})
