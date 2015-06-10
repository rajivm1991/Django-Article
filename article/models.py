from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    publication_date = models.DateTimeField()
    category = models.CharField(max_length=15)
    hero_image = models.ImageField(upload_to='hero_images')
    additional_image = models.ImageField(upload_to='additional_images', null=True, blank=True)
    body_text = models.TextField()

    def __str__(self):
        return self.title
