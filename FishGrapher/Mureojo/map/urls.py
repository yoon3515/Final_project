from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'map'

urlpatterns = [
    path('', views.get_fishing_spots, name='fishing_spots'),
    path('get_fishing_spots', views.get_fishing_spots, name='get_fishing_spots'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
