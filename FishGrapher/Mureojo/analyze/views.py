import io
import torch
import base64
from torchvision import transforms
from PIL import Image
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from fishBook.models import FishBook, CaughtFishInfo

def decode_image(data):
    # 'data:image/png;base64,' 부분 제거
    data = data.replace('data:image/png;base64,', '')
    # base64로 인코딩된 이미지 데이터 디코딩
    decoded_data = base64.b64decode(data)
    # PIL 이미지로 변환
    image = Image.open(io.BytesIO(decoded_data))
    return image


def predict_fish(image):
    # 불러온 모델 파일 경로
    model_path = 'analyze/fish_model2.pth'
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
    _, predicted = torch.max(output.data, 1)
    return predicted.item()


@csrf_exempt
def analyze(request):
    if request.method == 'POST':
        # POST 요청으로 받은 이미지 데이터 디코딩
        image = decode_image(request.POST['image'])
        # 이미지를 어종으로 판별
        fish_id = predict_fish(image)
        # 결과 반환
        return JsonResponse({'fish_id': fish_id, 'image': request.POST['image']})
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
