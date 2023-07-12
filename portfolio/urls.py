from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolio'

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('', include('gallery.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)