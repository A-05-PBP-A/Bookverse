from django.urls import path
from bv_overseer.views import show_overseer_main

app_name = 'bv_overseer'

urlpatterns = [
    path('', show_overseer_main, name='show_overseer_main'),
]