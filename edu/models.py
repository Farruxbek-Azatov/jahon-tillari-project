from django.db import models
from django.urls import reverse


class Subject(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('edu:subject_detail', args=[self.slug])


class ItemBase(models.Model):
    subject = models.ForeignKey(
        Subject, related_name='%(class)ss', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    course = models.CharField(
        max_length=1, default='1', choices=(('1', '1'), ('2', '2')))

    class Meta:
        abstract = True


class Book(ItemBase):
    book = models.FileField(
        upload_to=f'edu/books/')

    def __str__(self):
        return self.name


class Slide(ItemBase):
    slide = models.FileField(
        upload_to=f'edu/slides/')

    def __str__(self):
        return self.name


class Video(ItemBase):
    url = models.URLField()

    def __str__(self):
        return self.name


class OnlineLesson(models.Model):
    subject = models.ForeignKey(
        Subject, related_name='%(class)ss', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name
