from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    img = models.ImageField(upload_to='collective/category/')

    class Meta:
        verbose_name = 'Kafedra'
        verbose_name_plural = 'Kafedralar'

    def __str__(self):
        return self.name


class Employee(models.Model):
    category = models.ForeignKey(
        Category, related_name='employees', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    img = models.ImageField(upload_to='collective/employee')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name = 'Ishchi'
        verbose_name_plural = 'Ishchilar'

    def __str__(self):
        return self.full_name
