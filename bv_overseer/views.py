from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from bookProfile.models import Review, Book
from django.contrib.auth import get_user_model   
from .forms import AddBookForm, DeleteBookForm
from django.urls import reverse

def bv_overseer_view(request):
    reviews = Review.objects.all()
    users = User.objects.all()
    context = {'reviews': reviews,
               'users': users}
    return render(request, 'adminprofile.html', context)

def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            new_book = form.save()
            return HttpResponseRedirect(reverse('bv_overseer:bv_overseer_view'))
    else:   
        form = AddBookForm()

    return render(request, 'add_book.html', {'form': form})

def delete_book(request, book_id=None):
    book = get_object_or_404(Book, pk=book_id) if book_id else None

    if request.method == 'POST':
        form = DeleteBookForm(request.POST, instance=book)
        if form.is_valid():
            if book:
                book.delete()
                return redirect('bv_overseer:bv_overseer_view')
            else:
                return render(request, 'delete_book.html', {'error_message': 'No Book matches the given query.'})
    else:
        form = DeleteBookForm(instance=book)

    books = Book.objects.all()

    context = {'books': books, 'book_title': book.title if book else None, 'form': form}
    return render(request, 'delete_book.html', context)

User = get_user_model()

def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    
    if request.method == 'POST':
        review.delete()
        return HttpResponseRedirect(reverse('bv_overseer:bv_overseer_view'))