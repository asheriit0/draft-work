from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# admin.site.site_url = None

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace="users")),
    path('', include('dishlist.urls')),
    path('basket/', include('basket.urls', namespace='basket')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


