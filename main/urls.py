from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urls = list(admin.site.urls)

urls[0] +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urls[0] +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ [
path('', include('core.urls')),
path('web/', admin.site.urls),

# path('admin_tools_stats/', include('admin_tools_stats.urls')),

] 
admin.site.index_title = "Dashboard"
