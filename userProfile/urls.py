from django.urls import path
from userProfile.views import show_user_profile, edit_profile, add_to_favorites, get_user_favorite, change_password

app_name = 'userProfile'

urlpatterns = [
    path('user-profile/', show_user_profile, name='show_user_profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('add_to_favorites/<int:book_id>/', add_to_favorites, name='add_to_favorites'),
    path('change_password', change_password,name='change_password'),
    path('book_favorite/',get_user_favorite, name='get_user_favorite'),
]