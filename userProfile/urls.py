from django.urls import path
from userProfile.views import show_user_profile, edit_profile, add_to_favorites, get_user_favorite, change_password
from userProfile.views import add_to_favorites_flutter, get_user_favorite_flutter, delete_book,get_user_history_flutter
from userProfile.views import get_user_history

app_name = 'userProfile'

urlpatterns = [
    path('user-profile/', show_user_profile, name='show_user_profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('add_to_favorites/<int:book_id>/', add_to_favorites, name='add_to_favorites'),
    path('change_password', change_password,name='change_password'),
    path('book_favorite/',get_user_favorite, name='get_user_favorite'),
    path('favorite-flutter/',add_to_favorites_flutter, name='add_to_favorites_flutter'),
    path('book_favorite_flutter/<str:username>/', get_user_favorite_flutter, name='get_user_favorite_flutter'),
    path('delete_bookFav/<int:book_id>/', delete_book, name='delete_book'),
    path('book_history_flutter/<str:username>/',get_user_history_flutter, name='get_user_history_flutter'),
    path('book_history/',get_user_history, name='get_user_history'),
]