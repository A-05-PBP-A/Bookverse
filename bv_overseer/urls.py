from django.urls import include, path
from bv_overseer.views import show_overseer_main, bv_overseer_view

app_name = 'bv_overseer'

urlpatterns = [
    path('bookProfile/', include('bookProfile.urls')),
    path('', bv_overseer_view, name='bv_overseer_view')
]