from django.urls import include, path
from bv_overseer.views import bv_overseer_view, add_book, delete_book, delete_review, get_user_flutter, get_reviews_flutter

app_name = 'bv_overseer'

urlpatterns = [
    path('adminpage/', bv_overseer_view, name='bv_overseer_view'),
    path('add_book/', add_book, name='add_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('delete_review/<int:review_id>/', delete_review, name='delete_review'),
    path('api/get_user_flutter/', get_user_flutter, name='get_user_flutter'),
    path('api/get_reviews_flutter/', get_reviews_flutter, name='get_reviews_flutter'),
]