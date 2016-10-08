from django.shortcuts import render, get_object_or_404
from .models import GalleryGroup, Artwork


def galleries(request):
    galleryGroups = GalleryGroup.objects.all().order_by('title')
    return render(request, 'gallery/galleries.html', {'galleryGroups': galleryGroups})


def gallery_detail(request, gallery_title_slug):
    context_dict = {}
    
    try:
        galleryGroups = GalleryGroup.objects.get(slug=gallery_title_slug)
        context_dict['galleryGroups'] = galleryGroups
        artworks = Artwork.objects.filter(group=galleryGroups).order_by('published_date')
        context_dict['artworks'] = artworks

    except GalleryGroup.DoesNotExist:
        pass

    return render(request, 'gallery/gallery_detail.html', context_dict)


def art_detail(request, art_id):
    artwork = get_object_or_404(Artwork, id=art_id)
    try:
        next = artwork.get_next_by_published_date()
        while (next.group != artwork.group):
            next = next.get_next_by_published_date()
    except Artwork.DoesNotExist:
        next = None

    try:
        previous = artwork.get_previous_by_published_date()
        while (previous.group != artwork.group):
            previous = previous.get_previous_by_published_date()
    except Artwork.DoesNotExist:
        previous = None

    return render(request, 'gallery/art_detail.html', {'artwork': artwork, 'next': next, 'previous': previous })


def about_me(request):
    return render(request, 'gallery/about_me.html')

