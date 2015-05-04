from django.conf.urls import patterns, include, url
from . import views


urlpatterns = [
    url(r'^$', views.galleries, name='home'),
    url(r'^gallery/(?P<gallery_title_slug>[\w\-]+)/', views.gallery_detail, name='gallery_detail'),
    url(r'^art/(?P<art_id>[0-9]+)/$', views.art_detail, name='art'),
    url(r'^about/$', views.about_me, name="aboutMe"),
]

