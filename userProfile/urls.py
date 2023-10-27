from django.urls import path
from userProfile.views import show_user_profile

app_name = 'userProfile'

urlpatterns = [
    path('', show_user_profile, name='show_user_profile'),
]