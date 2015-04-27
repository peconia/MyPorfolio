from django.shortcuts import render
from .models import GalleryGroup, Artwork

def galleries(request):
    galleryGroups = GalleryGroup.objects.all().order_by('title')
    return render(request, 'gallery/galleries.html', { 'galleryGroups': galleryGroups })
