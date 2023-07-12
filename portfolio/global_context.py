from gallery.models import GalleryGroup

def add_to_context(request):
    gallery_groups = GalleryGroup.objects.all().order_by('title')

    context = {
        'gallery_groups': gallery_groups
    }

    return context
