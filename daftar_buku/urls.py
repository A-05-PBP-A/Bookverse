from django.urls import path
from daftar_buku.views import show_main, get_books_json, filter_books
#from auth.views import login_user, logout_user

app_name = 'daftar_buku'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-books/', get_books_json, name='get_books_json'),
    path('filter-books/', filter_books, name='filter_books')
]