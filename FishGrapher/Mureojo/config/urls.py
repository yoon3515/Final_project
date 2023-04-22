from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from map.views import get_fishing_spots

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('map/', include('map.urls')),
    path('get_fishing_spots/', get_fishing_spots, name='get_fishing_spots'),
    path('fishBook/', include('fishBook.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
