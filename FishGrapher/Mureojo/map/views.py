import json
import pymongo
from django.shortcuts import render
from .models import FishingSpot

def get_fishing_spots(request):
    # MongoDB에 연결
    client = pymongo.MongoClient('mongodb://localhost:27017/')

    # 데이터베이스 선택
    db = client['mul_db']

    # 컬렉션 선택
    collection = db['fishing_spots']

    # 데이터 검색
    spots = collection.find()

    markers = []
    for spot in spots:
        marker = {
            'name': spot['name'],
            'address': spot['address'],
            'lat': spot['lat'],
            'lng': spot['lng'],
        }
        markers.append(marker)

    markers_json = json.dumps(markers)

    KAKAO_MAP_API_KEY = '50e62e5f254634adaf3d813b56794396'
    return render(request, 'map/fishing_spots.html', {
        'markers_json': markers_json,
        'kakao_map_api_key': KAKAO_MAP_API_KEY,
    })
