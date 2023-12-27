from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('web/', admin.site.urls),
path('', include('core.urls'))
]
admin.site.index_title = "Dashboard"
# admin.site.site_header

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)