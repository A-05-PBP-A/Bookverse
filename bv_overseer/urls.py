from django.urls import include, path
from bv_overseer.views import bv_overseer_view, add_book, delete_review, delete_user

app_name = 'bv_overseer'

urlpatterns = [
    path('adminpage/', bv_overseer_view, name='bv_overseer_view'),
    path('add_book/', add_book, name='add_book'),
    path('delete_review/<int:review_id>/', delete_review, name='delete_review'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
]