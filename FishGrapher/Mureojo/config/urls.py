from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from map.views import get_fishing_spots
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='main.html'), name='home'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('map/', include('map.urls')),
    path('get_fishing_spots/', get_fishing_spots, name='get_fishing_spots'),
    path('pictures/', include('pictures.urls'), name='pictures'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
