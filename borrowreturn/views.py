from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from borrowreturn.forms import BorrowingForm
from borrowreturn.models import Borrowing
from bookProfile.models import Book
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.utils import timezone

@login_required(login_url='/login/')
def borrow_book(request):
    form = BorrowingForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.book = Book.objects.get(pk=request.POST.get('book'))
        product.book_title = product.book.title
        product.image_url_l = product.book.image_url_l
        product.reference_id = product.book.pk
        product.save()
        return HttpResponseRedirect(reverse('borrowreturn:show_borrowing'))
    books = Book.objects.all()
    context = {'form': form, 'books': books}
    return render(request, "add_borrowing.html", context)

# def borrow_spesific_book(request, book_id):
#     form = BorrowingForm(request.POST or None)

#     if form.is_valid() and request.method == "POST":
#         product = form.save(commit=False)
#         product.user = request.user
#         product.save()
#         return HttpResponseRedirect(reverse('borrowreturn:show_borrowing'))
    
#     book = Book.objects.get(id=book_id)
#     context = {'form': form, 'book': book}
#     return render(request, "add_borrowing.html", context)

def show_borrowing(request):
    items = Borrowing.objects.filter(user=request.user, is_returned = False)
    # print(items)
    context = {
        'appname': 'Bookverse',
        'name': request.user.username,
        'items': items
    }

    return render(request, "show_borrowing.html", context)

def get_book_cover(request, book_id):
    book = Book.objects.get(id=book_id)
    return JsonResponse({'cover_url': book.cover_url})

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
    filtered_books = Borrowing.objects.all().filter(book_title__icontains=keyword)
   

    return HttpResponse(serializers.serialize('json', filtered_books))