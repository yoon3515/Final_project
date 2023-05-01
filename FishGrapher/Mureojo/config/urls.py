from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='main.html'), name='home'),
    # path('', TemplateView.as_view(template_name='before_main.html'), name='home'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('map/', include('map.urls')),
    path('fishBook/', include('fishBook.urls')),
    path('fish_info/', include('fish_info.urls')),
    # path('search/', include('search.urls')),
    # path('analyze/', include('analyze.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
