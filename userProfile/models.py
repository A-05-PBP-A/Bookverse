from django.db import models
from bookProfile.models import Book, Review
from django.contrib.auth.models import User

# Create your models here.
class Pengguna(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    booksHistory = models.ManyToManyField(Book, related_name='books_history', blank=True)
    borrowedBooks = models.ManyToManyField(Book, related_name='borrowed_book', blank=True)
    favoriteBooks = models.ManyToManyField(Book, related_name='favorite_books', blank=True)
    reviewsHistory = models.ManyToManyField(Review, related_name='reviews_history', blank=True)

    def add_book_to_history(self, book):
        self.booksHistory.add(book)

    def add_book_to_borrowed(self, book):
        self.borrowedBooks.add(book)

    def add_book_to_favorites(self, book):
        self.favoriteBooks.add(book)

    def add_review_to_history(self, review):
        self.reviewsHistory.add(review)
