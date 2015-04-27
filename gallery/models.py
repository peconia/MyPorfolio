from django.db import models


class GalleryGroup(models.Model):

    title = models.CharField(max_length=100, default='')
    description = models.TextField()

    def __str__(self):
        return self.title
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
    art = models.ImageField(upload_to="media/art")
    group = models.ForeignKey('GalleryGroup')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
