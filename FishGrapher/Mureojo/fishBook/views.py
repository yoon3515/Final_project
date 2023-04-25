from django.shortcuts import render
from .models import FishBook

# Create your views here.
# fishBook/views.py
def fish_book_list(request):
    fish_books = FishBook.objects.all()
    return render(request, 'fishBook/book.html', {'fish_books': fish_books})



def save_fish_book(request):
    if request.method == 'POST':
        fish_name = request.POST['fish_name']
        image_url = request.POST['image_url']

        # 중복 검사
        if FishBook.objects.filter(fish_name=fish_name).exists():
            # 이미 존재하는 정보인 경우 카운트를 증가시킨다.
            fish_book = FishBook.objects.get(fish_name=fish_name)
            fish_book.count += 1
            fish_book.save()
        else:
            # 새로운 정보인 경우 새로운 카드를 생성한다.
            fish_book = FishBook.objects.create(fish_name=fish_name, image_url=image_url)
            # fish_book.save()

    return redirect('fishBook:fish_book_list')
