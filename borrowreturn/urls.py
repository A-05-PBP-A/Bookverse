from django.urls import path
from borrowreturn.views import *

app_name = 'borrowreturn'

urlpatterns = [
    path('borrow/', borrow_book, name='borrow_book'),
    path('my-borrowing/', show_borrowing, name='show_borrowing'),
    path('borrowing-data/',get_user_borrowing, name='get_user_borrowing' ),
    path('book-data/<int:book_id>/', get_book_by_id, name='get_book_by_id'),
    path('return-borrowing/<int:borrowing_id>/', return_borrowing, name='return_borrowing'),
    path('filter-borrowings/', filter_borrowings, name='filter_borrowings'),
    path('return-flutter/<str:username>/', return_borrowing_flutter, name='return_borrowing_flutter'),
    path('borrow-flutter/', borrow_book_flutter, name='borrow_book_flutter'),
    path('get-book-cover/', get_book_url, name='get_book_url'),
    path('filter-flutter/', filter_borrowings_flutter, name='filter_borrowings_flutter')
]