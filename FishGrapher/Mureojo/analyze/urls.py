from django.urls import path
from . import views
from django.conf.urls.static import static
from config import settings

app_name = 'analyze'

urlpatterns = [
	path('', views.today_fish, name='today_fish'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 개발환경에서 미디어 파일 제공을 위한 URL 패턴 추가
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)