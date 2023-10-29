from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=13, null= True, blank = True)
    title = models.CharField(max_length=255, null= True, blank = True)
    author = models.CharField(max_length=255, null= True, blank = True)
    publication_year = models.IntegerField(null= True, blank = True)
    publisher = models.CharField(max_length=255, null= True, blank = True )
    image_url_s = models.URLField(null= True, blank = True)
    image_url_m = models.URLField(null= True, blank = True)
    image_url_l = models.URLField(null= True, blank = True)

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review = models.CharField(max_length=500)
