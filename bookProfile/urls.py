from django.urls import path
from bookProfile.views import show_profile, get_books

app_name = 'bookProfile'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path("books/", get_books, name="get_books")
]