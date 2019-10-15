from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('gallery.urls')),
    #This is the setting configuration of the setting.py for making the media file accessible django .
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

