from django.db import models
from django.urls.base import reverse
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    created = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = 'Tadbir'
        verbose_name_plural = 'Tadbirlar'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('galery:event_detail', args=[self.slug])


class Image(models.Model):
    event = models.ForeignKey(
        Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasmlar'
