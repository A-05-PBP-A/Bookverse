from django.urls import path
from flutterauth.views import register, login, logout

app_name = 'flutterauth'

urlpatterns = [
    path('login_flutter/', login, name='login'),
    path('logout_flutter/', logout, name='logout'),
    path('register_flutter/', register, name='register'),
]