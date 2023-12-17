from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    isbn = models.CharField(max_length=13, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    publication_year = models.IntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    image_url_s = models.URLField(null=True, blank=True)
    image_url_m = models.URLField(null=True, blank=True)
    image_url_l = models.URLField(null=True, blank=True)