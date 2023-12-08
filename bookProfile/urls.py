from django.urls import path
from bookProfile.views import show_review, get_books, get_review_json, add_review_ajax, show_review_json, show_review_xml, show_review_json_by_id, show_review_xml_by_id, get_book_by_id

app_name = 'bookProfile'

urlpatterns = [
    path('book/<int:book_id>/', show_review, name='show_review'),
    path("books/", get_books, name="get_books"),
    path('get_review_json/<int:book_id>/', get_review_json, name='get_review_json'),
    path('create-item-ajax/', add_review_ajax, name='add_review_ajax'),
    path('json/', show_review_json, name='show_review_json'), 
    path('xml/', show_review_xml, name='show_review_xml'), 
    path('json/<int:id>/', show_review_json_by_id, name='show_review_json_by_id'), 
    path('xml/<int:id>/', show_review_xml_by_id, name='show_review_xml_by_id'),
    path('api/<int:book_id>/', get_book_by_id, name='get_book_by_id'),
]