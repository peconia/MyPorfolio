from django.urls import re_path
from . import views

app_name = 'gallery'

urlpatterns = [
    re_path(r'^$', views.galleries, name='home'),
    re_path(r'^gallery/(?P<gallery_title_slug>[\w\-]+)/', views.gallery_detail, name='gallery_detail'),
    re_path(r'^art/(?P<gallery_title_slug>[\w\-]+)/(?P<art_id>[0-9]+)/$', views.art_detail, name='art'),
    re_path(r'^about/$', views.about_me, name="aboutMe"),
]

handler404 = views.handle_404