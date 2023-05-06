from . import views
from config import settings
from django.conf.urls.static import static
from django.urls import path

app_name = 'analyze'

urlpatterns = [
	path('camera/', views.analyze, name='camera'),
    path('today_fish/', views.today_fish, name='today_fish')
]

# 개발환경에서 미디어 파일 제공을 위한 URL 패턴 추가
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
