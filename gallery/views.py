from django.shortcuts import render, get_object_or_404
from .models import GalleryGroup, Artwork


def handle_404(request, exception):
    return render(request, '404.html', context={})


def galleries(request):
    featured_works = Artwork.objects.filter(featured=True)
    
    context = { 
        'featured_works': featured_works
    }
    
    return render(request, 'gallery/galleries.html', context)


def gallery_detail(request, gallery_title_slug):
    context = {}
    try:
        gallery_group = GalleryGroup.objects.get(slug=gallery_title_slug)
        artworks = Artwork.objects.filter(group=gallery_group).order_by('published_date')

        context['gallery_title_slug'] = gallery_title_slug
        context['gallery_group'] = gallery_group
        context['artworks'] = artworks
    except GalleryGroup.DoesNotExist:
        pass

    return render(request, 'gallery/gallery_detail.html', context)


def art_detail(request, gallery_title_slug, art_id,):
    artwork = get_object_or_404(Artwork, id=art_id)
    try:
        next_artwork = artwork.get_next_by_published_date()
        while next_artwork.group != artwork.group:
            next_artwork = next_artwork.get_next_by_published_date()
    except Artwork.DoesNotExist:
        next_artwork = None

    try:
        previous = artwork.get_previous_by_published_date()
        while previous.group != artwork.group:
            previous = previous.get_previous_by_published_date()
    except Artwork.DoesNotExist:
        previous = None

    context = {
        'gallery_title_slug': gallery_title_slug,
        'artwork': artwork,
        'next': next_artwork,
        'previous': previous
    }

    return render(request, 'gallery/art_detail.html', context)


def about_me(request):
    return render(request, 'gallery/about_me.html')

