from django.urls import include, path
from bv_overseer.views import show_overseer_main, bv_overseer_view
from . import views

app_name = 'bv_overseer'

urlpatterns = [
    path('', bv_overseer_view, name='bv_overseer_view'),
    path('add_book/', views.add_book, name='add_book'),
]