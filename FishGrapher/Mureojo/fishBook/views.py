from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import FishBook, CaughtFishInfo
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# from django.contrib.auth.models import User


# Create your views here.
# fishBook/views.py


def save_fish(request):
    if request.method == 'POST':
        fish_name = request.POST['fish_name']
        image_url = request.POST['image_url']

        # 중복 검사
        if CaughtFishInfo.objects.filter(fish_name=fish_name).exists():
            # 이미 존재하는 정보인 경우 카운트를 증가시킨다.
            caught_fishes = CaughtFishInfo.objects.get(fish_name=fish_name)
            caught_fishes.count += 1
            caught_fishes.save()
        else:
            # 새로운 정보인 경우 새로운 카드를 생성한다.
            caught_fishes = CaughtFishInfo.objects.create(fish_name=fish_name, image_url=image_url)
            caught_fishes.save()

    return redirect('fishBook:save_fish')



@login_required
def my_caught_fish_list(request):
    # 현재 로그인한 사용자 정보 가져오기
    user = request.user

    # 현재 로그인한 사용자가 잡은 모든 물고기 정보 가져오기
    caught_fishes = CaughtFishInfo.objects.filter(member=user)

    # 물고기 정보와 일치하는 FishBook 정보 가져오기
    fish_books = []
    for fish in caught_fishes:
        fish_book = FishBook.objects.filter(fish_name=fish.fish_book.fish_name).first()
        if fish_book:
            fish_books.append(fish_book)

    return render(request, 'fishBook/book.html', {'caught_fishes': caught_fishes, 'fish_books': fish_books})


def search_fish(request):
    if request.method == 'POST':
        search_keyword = request.POST.get('search_keyword')
        if search_keyword:
            result_fishes = FishBook.objects.filter(fish_name__contains=search_keyword).first()
            if result_fishes:
                return render(request, 'fishBook/search_fish.html', {'result_fishes': result_fishes})
    return render(request, 'fishBook/book.html')


# @login_required
# def my_caught_fish_list(request):
#     # 현재 로그인한 사용자 정보 가져오기
#     User = get_user_model()
#     pk = request.user.pk
#     user = get_object_or_404(User, pk=pk)
#     # user = request.User
#
#     # 현재 로그인한 사용자가 잡은 모든 물고기 정보 가져오기
#     caught_fishes = CaughtFishInfo.objects.filter(member=user)
#     # 물고기 정보와 일치하는 FishBook 정보 가져오기
#     fish_books = []
#     for fish in caught_fishes:
#         fish_book = FishBook.objects.filter(fish_name=fish.fish_book.fish_name).first()
#         if fish_book:
#             fish_books.append(fish_book)
#     return render(request, 'fishBook/book.html', {'caught_fishes': caught_fishes, 'fish_books': fish_books})
