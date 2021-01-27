from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from infrastructure.views import start_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('infrastructure.urls')),
    path('', start_redirect),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
