from django.shortcuts import render
from .models import FishBook, CaughtFishInfo
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.
# fishBook/views.py


@login_required
def my_caught_fish_list(request):
    # 현재 로그인한 사용자 정보 가져오기
    user = request.user

    # 현재 로그인한 사용자가 잡은 모든 물고기 정보 가져오기
    caught_fishes = CaughtFishInfo.objects.filter(member=user)

    # 중복을 제거한 fish_name 가져오기
    fish_names = (
        CaughtFishInfo.objects.filter(member=user)
        .values('fish_book__fish_name')
        .annotate(count=Count('id'))
        .order_by('fish_book__fish_name')
        .distinct()
    )

    # FishBook 정보 가져오기
    fish_books = []
    for fish_name in fish_names:
        fish_book = FishBook.objects.filter(fish_name=fish_name['fish_book__fish_name']).first()
        if fish_book:
            fish_book.count = fish_name['count']
            fish_books.append(fish_book)

    return render(request, 'fishBook/book.html', {'caught_fishes': caught_fishes, 'fish_books': fish_books})



def search_fish(request):
    query = request.GET.get('search')
    result_fishes = CaughtFishInfo.objects.none()
    result_fish_books = []
    if query:
        result_fishes = CaughtFishInfo.objects.filter(fish_book__fish_name__icontains=query)
        for fish in result_fishes:
            fish_book = FishBook.objects.filter(fish_name=fish.fish_book.fish_name).first()
            if fish_book:
                result_fish_books.append(fish_book)

    no_result = not result_fishes and query is not None

    return render(request, 'fishBook/book_result.html', {'query': query, 'result': result_fishes, 'result_fish_books': result_fish_books, 'no_result': no_result})


# def search_fish(request):
#     query = request.GET.get('search')
#     result_fishes = CaughtFishInfo.objects.none()
#     if query:
#         result_fishes = CaughtFishInfo.objects.filter(fish_book__fish_name__icontains=query)
#     return render(request, 'fishBook/book_result.html', {'query': query, 'result': result_fishes, 'no_result': query and not result_fishes})


# def search_fish(request):
#     query = request.GET.get('search')
#     result_fishes = CaughtFishInfo.objects.none()
#     if query:
#         result_fishes = CaughtFishInfo.objects.filter(fish_book__fish_name__icontains=query)
#     return render(request, 'fishBook/book_result.html', {'query': query, 'result': result_fishes})
#
#
# def fish_info(request, fish_id):
#     fish = get_object_or_404(FishBook, pk=fish_id)
#     caught_fish = CaughtFishInfo.objects.filter(fish=fish_id)
#     return render(request, 'fish_info/fish_info.html', {'fish': fish, 'caught_fish': caught_fish})


