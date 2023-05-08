import datetime
import io
import torch
import os
from .models import FishImages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from fish_info.models import FishBook, CaughtFishInfo
from PIL import Image
from torchvision import transforms


def decode_image(data):
    # 이미지 데이터 로드
    decoded_data = data.read()
    # PIL 이미지로 변환
    image = Image.open(io.BytesIO(decoded_data))
    return image


def predict_fish(image):
    # 불러온 모델 파일 경로
    model_path = 'analyze/20230420_Resnet_color10-nogray.pt'
    # 불러온 모델을 CPU에 로드
    model = torch.load(model_path, map_location=torch.device('cpu'))
    print(type(model))
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
    _, predicted = torch.max(output.data, 1)
    return predicted.item()


@login_required
@csrf_exempt
def analyze(request):
    if request.method == 'POST':
        # POST 요청으로 받은 이미지 데이터 디코딩
        image = decode_image(request.FILES['image'])
        # 이미지를 어종으로 판별
        fish_id = predict_fish(image)

        # 이미지를 서버에 저장
        user_id = request.user.id

        fish_book = FishBook.objects.get(id=fish_id+12)

        # fish_book 이용, 정보 가져와서 caughtfishinfo 테이블 생성
        caught_fish = CaughtFishInfo(member=request.user, fish_book=fish_book, caught_date=datetime.date.today())
        caught_fish.save()
        # 새로 생성된 객체의 ID 가져오기
        caught_fish_id = caught_fish.id
        # 새로운 이미지 파일 생성
        image_name = f"{user_id}_{fish_id}_{caught_fish_id}.png"
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)
        if request.method == 'POST':
            image_file = request.FILES.get('image')
            with Image.open(image_file) as img:
                img.save(image_path, format="PNG")
        # 테이블에 이미지 주소 저장
        caught_fish.myfish_photo = f"{settings.MEDIA_ROOT}{image_name}"
        caught_fish.save()

        # 결과 반환
        return JsonResponse({'fish_id': fish_id, 'image_name': image_name})
    else:
        return render(request, 'analyze/camera.html')


def today_fish(request):
    # analyze 앱의 analyze 뷰에서 넘겨받은 어종 ID와 찍은 사진 데이터
    fish_id = request.GET.get('fish_id')
    image_data = request.GET.get('image')
    # 어종 ID에 해당하는 어종 정보 조회 (이미지, 이름, 설명 등)
    fish = FishBook.objects.get(pk=fish_id)
    # 결과 정보를 딕셔너리 형태로 저장
    result = {
        'name': fish.name,
        'habitat':fish.habitat,
        'distribution':fish.distribution,
        'limit_start':fish.limit_start,
        'limit_end':fish.limit_end,
        'prohibition_size':fish.prohibition_size,
        'image': image_data
    }
    return render(request, 'analyze/todayFish.html', {'result': result})
