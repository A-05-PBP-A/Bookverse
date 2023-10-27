from django.db import models
from bookProfile.models import Book, Review

# Create your models here.
class Pengguna(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    booksHistory = models.ManyToManyField(Book, related_name='books_history')
    favoriteBooks = models.ManyToManyField(Book, related_name='favorite_books')
    reviewsHistory = models.ManyToManyField(Review, related_name='reviews_history')