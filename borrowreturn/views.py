from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from borrowreturn.forms import BorrowingForm
from borrowreturn.models import Borrowing
from bookProfile.models import Book
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.utils import timezone

@login_required(login_url='/login/')
def borrow_book(request):
    form = BorrowingForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        book = Book.objects.get(pk=request.POST.get('book'))
        now = timezone.now()
        # mencari semua buku yang belum dikembalikan oleh user dan melebihi return_date
        overdue_books = Borrowing.objects.filter(user = request.user, is_returned=False, return_date__lt=now)
        # Cek apakah buku ini sudah dipinjam oleh user dan belum dikembalikan
        existing_borrowing = Borrowing.objects.filter(user=request.user, book=book, is_returned=False)
        if existing_borrowing.exists():
            messages.error(request, 'You have already borrowed that book and it has not been returned yet.')
        elif overdue_books.exists():
            messages.error(request, 'You have overdue book(s). Please return them before borrowing another one.')
        else:
            product = form.save(commit=False)
            product.user = request.user
            product.book = book
            product.book_title = product.book.title
            product.image_url_l = product.book.image_url_l
            product.reference_id = product.book.pk
            product.save()
            return HttpResponseRedirect(reverse('borrowreturn:show_borrowing'))
    
    books = Book.objects.all()
    context = {'form': form, 'books': books}
    return render(request, "add_borrowing.html", context)

def show_borrowing(request):
    items = Borrowing.objects.filter(user=request.user, is_returned = False)
    # print(items)
    context = {
        'appname': 'Bookverse',
        'name': request.user.username,
        'items': items
    }
    return render(request, "show_borrowing.html", context)

def get_book_by_id(request, book_id):
    data = Book.objects.filter(pk=book_id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_user_borrowing(request):
    items = Borrowing.objects.filter(user=request.user, is_returned = False)
    return HttpResponse(serializers.serialize('json', items))

@csrf_exempt
def return_borrowing(request, borrowing_id):
    if request.method == "PATCH":
        borrowing = Borrowing.objects.get(id= borrowing_id)
        borrowing.is_returned = True
        borrowing.real_return_date = timezone.now()
        borrowing.save()
        return HttpResponse(b"OK", status=200)
    
def filter_borrowings(request):
    keyword = request.GET.get('keyword', '')
    filtered_books = Borrowing.objects.filter(book_title__icontains=keyword, is_returned=False, user=request.user)
   
    return HttpResponse(serializers.serialize('json', filtered_books))