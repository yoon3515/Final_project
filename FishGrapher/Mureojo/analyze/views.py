import io
import torch
import os
from datetime import date
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from fish_info.models import FishBook, CaughtFishInfo
from PIL import Image
from torchvision import transforms


def decode_image(data):
    # 이미지 데이터 로드
    decoded_data = data.read()
    # PIL 이미지로 변환
    image = Image.open(io.BytesIO(decoded_data)).convert('RGB')
    return image


def predict_fish(image):
    # 불러온 모델 파일 경로
    model_path = 'analyze/1004.pt'
    # 불러온 모델을 CPU에 로드
    model = torch.load(model_path, map_location=torch.device('cpu'))
    # 이미지 전처리
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = transform(image)
    # 배치 차원 추가
    image = image.unsqueeze(0)
    # 모델 예측
    output = model(image)
    # 결과 반환
    predictvalue, predicted = torch.max(output.data, 1)
    if predictvalue.item() < 6:
        return -1  # 정확도가 떨어지면 -1을 반환, analyze에서 오류로 필터링
    return predicted.item()


@login_required
@csrf_exempt
def analyze(request):
    if request.method == 'POST':
        # POST 요청으로 받은 이미지 데이터 디코딩
        image = decode_image(request.FILES['image'])
        # 이미지를 어종으로 판별
        fish_id = predict_fish(image)
        if fish_id == -1:
            messages.error(request, '해당하는 물고기를 찾을 수 없습니다.')  # 정확도 떨어지는 사진 필터링
            return render(request, 'analyze/camera.html')
        else:
        # 이미지를 저장 (임시)
            user_id = request.user.id
            image_name = '{}_{}.jpg'.format(user_id, fish_id)
            image_path = os.path.join(settings.MEDIA_ROOT, 'caughtFish_image', image_name)
            image_file = request.FILES.get('image')
            with Image.open(image_file).convert('RGB') as img:
                img.save(image_path, format="jpeg")
            # 결과 반환
            redirect_url = reverse('analyze:today_fish')
            redirect_url += f'?user_id={user_id}&fish_id={int(fish_id)}&image={image_name}'
            return HttpResponseRedirect(redirect_url)
    else:
        return render(request, 'analyze/camera.html')


def today_fish(request):
    # analyze 앱의 analyze 뷰에서 넘겨받은 ID와 찍은 사진 데이터
    user_id = request.GET.get('user_id')
    fish_id = int(request.GET.get('fish_id'))
    image_name = request.GET.get('image')

    # fish_id 번호와 물고기가 할당된 테이블 번호 매핑
    id_map = {0: 16, 1: 20, 2: 12, 3: 21, 4: 13, 5: 14, 6: 17, 7: 18, 8: 19, 9: 15, 10: 22}
    fish_id = id_map.get(fish_id, fish_id)

    # 어종 ID에 해당하는 어종 정보 조회 (이미지, 이름, 설명 등)
    fish = FishBook.objects.get(id=fish_id)

    # caughtfishinfo 테이블 생성
    caught_fish = CaughtFishInfo(member=request.user, fish_book=fish, caught_date=date.today())
    caught_fish.save()

    # 새로 생성된 객체의 ID 가져오기
    caught_fish_id = caught_fish.id

    # 새로운 이미지 파일 생성
    image_name2 = f"{user_id}_{fish_id}_{caught_fish_id}.jpg"
    image_path = os.path.join(settings.MEDIA_ROOT, 'caughtFish_image', image_name2)
    image_file = os.path.join(settings.MEDIA_ROOT, 'caughtFish_image', image_name)
    with Image.open(image_file) as img:
        img.save(image_path, format="jpeg")

    # 테이블에 이미지 주소 저장
    caught_fish.myfish_photo = os.path.join(settings.MEDIA_URL, 'caughtFish_image', image_name2)
    caught_fish.save()

    # 결과 정보를 딕셔너리 형태로 저장
    result = {
        'id': fish.id,
        'name': fish.fish_name,
        'habitat': fish.habitat,
        'distribution': fish.distribution,
        'limit_start': fish.limit_start,
        'limit_end': fish.limit_end,
        'prohibition_size': fish.prohibition_size,
        'caught_date': date.today().strftime('%Y-%m-%d'),
        'image': image_name2,
    }
    os.remove(image_file)
    return render(request, 'analyze/todayFish.html', {'result': result})
