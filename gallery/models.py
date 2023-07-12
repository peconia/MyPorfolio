from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class GalleryGroup(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(blank=True, default='')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                super(GalleryGroup, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gallery.views.gallery_detail', args=[str(self.id)])


class Artwork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    published_date = models.DateTimeField(blank=True)
    art = models.ImageField(upload_to="art")
    group = models.ForeignKey('GalleryGroup', on_delete=models.CASCADE)
    featured = models.BooleanField(help_text='Feature this artwork on the home page')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery.views.art_detail', args=[str(self.id)])
