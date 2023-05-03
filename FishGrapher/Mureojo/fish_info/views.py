from django.shortcuts import render, get_object_or_404
from .models import FishBook, CaughtFishInfo
from django.contrib.auth.decorators import login_required

# Create your views here.


def fish_info(request, fish_id):
    fish = get_object_or_404(FishBook, pk=fish_id)
    fish.image_url = fish.image.url
    caught_fish = CaughtFishInfo.objects.filter(fish_book=fish_id, member=request.user).first()
    total_caught = CaughtFishInfo.objects.filter(fish_book=fish_id).count()
    # if caught_fish:
    #     caught_fish.image_url = caught_fish.myfish_photo
    return render(request, 'fish_info/fish_info.html',
                  {'fish': fish, 'caught_fish': caught_fish, 'total_caught': total_caught})

