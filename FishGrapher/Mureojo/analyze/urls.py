from django.urls import path
from . import views
<<<<<<< HEAD
=======
from django.conf.urls.static import static
from config import settings
>>>>>>> 30eb01fd05f30db1a1ac0b77c2960ff7212805d1

app_name = 'analyze'

urlpatterns = [
<<<<<<< HEAD
    path('camera/', views.analyze, name='camera'),
    path('todayfish/', views.today_fish, name='todayfish'),
]
=======
	path('', views.today_fish, name='today_fish'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 개발환경에서 미디어 파일 제공을 위한 URL 패턴 추가
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 30eb01fd05f30db1a1ac0b77c2960ff7212805d1
