from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from fish_info.models import FishBook, CaughtFishInfo
from django.contrib.auth.decorators import login_required

@login_required
def search(request):
    if request.method == 'POST':
        query = request.POST['search']
        fish_book = FishBook.objects.filter(fish_name__icontains=query).get() if FishBook.objects.filter(fish_name__icontains=query).exists() else None
        if fish_book:
            return redirect(reverse('fish_info', args=[fish_book.id]))
        else:
            fishes = FishBook.objects.filter(fish_name__icontains=query)
            return render(request, 'search/search.html', {'query': query, 'fishes': fishes})
    else:
        fishes = FishBook.objects.all()
        return render(request, 'search/search.html', {'fishes': fishes})



@login_required
def fish_info(request, fish_id):
    fish = FishBook.objects.get(id=fish_id)
    caught_fish = fish.caught_fish.filter(user=request.user)
    total_caught = caught_fish.count()
    context = {
        'fish': fish,
        'caught_fish': caught_fish,
        'total_caught': total_caught,
        'all_fish': FishBook.objects.all()
    }
    return render(request, 'fish_info/fish_info.html', context)
