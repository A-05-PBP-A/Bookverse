from django.db import models
from django.contrib.auth.models import User
from bookProfile.models import Book, Review

class Pengguna(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null = True)
    booksHistory = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books_history', blank=True, null=True)
    book_title = models.CharField(max_length=255, null= True, blank = True)
    image_url_l = models.URLField(null= True, blank = True)
    reference_id = models.IntegerField(null= True, blank = True)
    is_returned = models.BooleanField(default=True)

class UserFav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favoriteBooks = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorite_books', blank=True, null=True)

class UserReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewsHistory = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='reviews_history', blank=True, null=True)