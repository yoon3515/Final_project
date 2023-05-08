from django.shortcuts import render, get_object_or_404, redirect
from .models import FishBook, CaughtFishInfo
from django.contrib.auth.decorators import login_required

# Create your views here.


def fish_info(request, fish_id):
    fish = get_object_or_404(FishBook, pk=fish_id)
    fish.image_url = fish.image.url
    caught_fish = CaughtFishInfo.objects.filter(fish_book=fish_id, member=request.user)
    total_caught = CaughtFishInfo.objects.filter(fish_book=fish_id).count()
    return render(request, 'fish_info/fish_info.html',
                  {'fish': fish, 'caught_fish': caught_fish, 'total_caught': total_caught})
    
@login_required
def fish_info_search(request):
    query = request.GET.get('search')
    fishes = FishBook.objects.filter(fish_name__icontains=query)
    if len(fishes) == 1:
        # 검색 결과가 하나인 경우 해당 물고기 정보 페이지로 redirect
        return redirect('fish_info:fish_info', fish_id=fishes[0].id)
    return render(request, 'search/search.html', {'fishes': fishes})
