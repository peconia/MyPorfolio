from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

class GalleryGroup(models.Model):

    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                super(GalleryGroup, self).save(*args, **kwargs)

   # def get_absolute_url(self, show="thumbnails"):
    #    return reverse2("group", dpk=self.pk, show=show)

    def get_absolute_url(self):
        return reverse('gallery.views.gallery_detail', args=[str(self.id)])
'''
    link = URLField(blank=True, null=True)


    def __unicode__(self):
        return self.title

    def get_absolute_url(self, show="thumbnails"):
        return reverse2("group", dpk=self.pk, show=show)

    def image_links(self):
        lst = [img.image.name for img in self.images.all()]
        lst = [link % ( settings.MEDIA_URL+img, basename(img) ) for img in lst]
        return ", ".join(lst)
    image_links.allow_tags = True
'''

class Artwork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)
    art = models.ImageField(upload_to="art")
    group = models.ForeignKey('GalleryGroup')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery.views.art_detail', args=[str(self.id)])
