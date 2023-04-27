from django.shortcuts import render, get_object_or_404
from .models import FishBook, MyCaughtFish
from django.contrib.auth.decorators import login_required

# Create your views here.


def fish_info(request, fish_id):
    fish = get_object_or_404(FishBook, pk=fish_id)
    caught_fish = MyCaughtFish.objects.filter(fish=fish_id)
    return render(request, 'fish_info/fish_info.html', {'fish': fish, 'caught_fish': caught_fish})
