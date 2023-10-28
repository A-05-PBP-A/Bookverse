from django.db import models

# Create your models here.
class Review(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    isbn = models.CharField(max_length=13, null= True, blank = True)
    title = models.CharField(max_length=255, null= True, blank = True)
    author = models.CharField(max_length=255, null= True, blank = True)
    publication_year = models.IntegerField(null= True, blank = True)
    publisher = models.CharField(max_length=255, null= True, blank = True )
    image_url_s = models.URLField(null= True, blank = True)
    image_url_m = models.URLField(null= True, blank = True)
    image_url_l = models.URLField(null= True, blank = True)