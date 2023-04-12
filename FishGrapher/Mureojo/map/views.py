import os
import pandas as pd
import folium
from django.conf import settings
from django.shortcuts import render

def show_map(request):
    # CSV 파일 읽기
    csv_file = os.path.join(settings.BASE_DIR, 'map', 'mapdata', 'map_coordinate.csv') # 파일 경로 수정
    df = pd.read_csv(csv_file)

    # 지도 생성
    center = [df['latitude'].mean(), df['longtitude'].mean()]  # 데이터의 중심을 지도 중심으로 설정
    m = folium.Map(location=center, zoom_start=10)

    # 핀마크로 위치 데이터 표시
    for index, row in df.dropna(subset=['latitude', 'longtitude']).iterrows():  # 결측치를 제외하고 데이터를 반복
        tooltip = str(row['area_name']) + ' - ' + str(row['address'])  # 숫자를 문자열로 변환하여 더해줌
        folium.Marker([row['latitude'], row['longtitude']], tooltip=tooltip).add_to(m)

    # 지도 출력
    m = m._repr_html_()
    context = {'map': m, 'center': center} # 'center' 변수 추가

    return render(request, 'map.html', context)
