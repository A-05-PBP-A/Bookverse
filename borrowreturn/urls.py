from django.urls import path
from borrowreturn.views import borrow_book, get_book_by_id, show_borrowing, get_user_borrowing, return_borrowing, filter_borrowings
app_name = 'borrowreturn'

urlpatterns = [
    # path('tes/', add_borrowing, name='show_landing'),
    path('borrow/', borrow_book, name='borrow_book'),
    path('my-borrowing/', show_borrowing, name='show_borrowing'),
    path('borrowing-data/',get_user_borrowing, name='get_user_borrowing' ),
    # path('borrow/<int:book_id>/', add_borrowing, name='add_borrowing'),
    path('book-data/<int:book_id>/', get_book_by_id, name='get_book_by_id'),
    path('return-borrowing/<int:borrowing_id>/', return_borrowing, name='return_borrowing'),
    path('filter-borrowings/', filter_borrowings, name='filter_borrowings')
]