from django.urls import path
from bookProfile.views import show_review, get_books, get_review_json, add_review_ajax, show_json

app_name = 'bookProfile'

urlpatterns = [
    path('', show_review, name='show_review'),
    path("books/", get_books, name="get_books"),
    path('get-review/', get_review_json, name='get_review_json'),
    path('create-item-ajax/', add_review_ajax, name='add_review_ajax'),
    path('json/', show_json, name='show_json'), 
]