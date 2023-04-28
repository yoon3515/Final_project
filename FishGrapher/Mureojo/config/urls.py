from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from map.views import get_fishing_spots

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('map/', include('map.urls')),
    path('get_fishing_spots/', get_fishing_spots, name='get_fishing_spots'),
<<<<<<< HEAD
    path('fishBook/', include('fishBook.urls')),
    path('fish_info/', include('fish_info.urls')),
=======
    path('search/', views.search_view, name='search'),
>>>>>>> 74e3b867fb7fbf54919ce93adc9990453898c570
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
