from django.urls import path
from userProfile.views import show_user_profile, show_edit_profile
from authentication.views import show_landing, register, login_user, logout_user

app_name = 'userProfile'

urlpatterns = [
    path('', show_user_profile, name='show_user_profile'),
    path('edit-profile/', show_edit_profile, name='show_edit_profile'),
]