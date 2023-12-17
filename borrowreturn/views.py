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
from userProfile.models import UserHistory
from userProfile.forms import bookHistoryForm
import json

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

#untuk halaman borrowing flutter
@csrf_exempt
def get_user_borrowing(request):
    items = Borrowing.objects.filter(user=request.user, is_returned = False)
    return HttpResponse(serializers.serialize('json', items), content_type="application/json")

@csrf_exempt
def return_borrowing(request, borrowing_id):
    formHistory = bookHistoryForm(None)
    if request.method == "PATCH":
        borrowing = Borrowing.objects.get(id= borrowing_id)
        borrowing.is_returned = True
        book = borrowing.book
        
        existing_History = UserHistory.objects.filter(user=request.user, book=book)

        #untuk menambah ke history setelah di return
        if not existing_History.exists():
            bookHistory = formHistory.save(commit=False)
            bookHistory.user = request.user
            bookHistory.book = book
            bookHistory.book_title = bookHistory.book.title
            bookHistory.image_url_l = bookHistory.book.image_url_l
            bookHistory.reference_id = bookHistory.book.pk
            bookHistory.save()
            
        borrowing.real_return_date = timezone.now()
        borrowing.save()
        return HttpResponse(b"OK", status=200)
    
def filter_borrowings(request):
    keyword = request.GET.get('keyword', '')
    filtered_books = Borrowing.objects.filter(book_title__icontains=keyword, is_returned=False, user=request.user)
   
    return HttpResponse(serializers.serialize('json', filtered_books))

@csrf_exempt
def return_borrowing_flutter(request):
    formHistory = bookHistoryForm(None)
    if request.method == 'POST':
        data = json.loads(request.body)
        borrowing_id = int(data["id"])
        borrowing = Borrowing.objects.get(id = borrowing_id)
        book = borrowing.book
        borrowing.is_returned = True

        # existing_History = UserHistory.objects.filter(user=request.user, book=book)

        # #untuk menambah ke history setelah di return
        # if not existing_History.exists():
        #     bookHistory = formHistory.save(commit=False)
        #     bookHistory.user = request.user
        #     bookHistory.book = book
        #     bookHistory.book_title = bookHistory.book.title
        #     bookHistory.image_url_l = bookHistory.book.image_url_l
        #     bookHistory.reference_id = bookHistory.book.pk
        #     bookHistory.save()
            
        borrowing.real_return_date = timezone.now()
        borrowing.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def borrow_book_flutter(request):
    form = BorrowingForm(request.POST or None)
    if request.method == 'POST':
        now = timezone.now()
        data = json.loads(request.body)
        book = Book.objects.get(pk=data["book"])
        now = timezone.now()
        # mencari semua buku yang belum dikembalikan oleh user dan melebihi return_date
        overdue_books = Borrowing.objects.filter(user = request.user, is_returned=False, return_date__lt=now)
        # Cek apakah buku ini sudah dipinjam oleh user dan belum dikembalikan
        existing_borrowing = Borrowing.objects.filter(user=request.user, book=book, is_returned=False)
        if existing_borrowing.exists():
            return JsonResponse({'message': 'You have already borrowed this book and it has not been returned yet.', 'status': 'error'}, status=400)
        elif overdue_books.exists():
            return JsonResponse({'message': 'You have overdue book(s). Please return them before borrowing another one.', 'status': 'error'}, status=400)
        else:
            new_borrowing = form.save(commit=False)
            new_borrowing.user = request.user
            new_borrowing.book = book
            new_borrowing.book_title = new_borrowing.book.title
            new_borrowing.image_url_l = new_borrowing.book.image_url_l
            new_borrowing.reference_id = new_borrowing.book.pk
            new_borrowing.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def get_book_url(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book_id = int(data["id"])
        book = Book.objects.get(id = book_id)
        book_url = book.image_url_l

        return JsonResponse({"url": book_url}, status = 200)