from django.urls import path
from authentication.views import show_landing, register, login_user, logout_user

app_name = 'authentication'

urlpatterns = [
    path('tes/', show_landing, name='show_landing'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
]