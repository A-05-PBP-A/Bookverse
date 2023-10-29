from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from bookProfile.models import Review, Book
from django.contrib.auth import get_user_model   
from .forms import AddBookForm
from django.urls import reverse

def bv_overseer_view(request):
    reviews = Review.objects.all()  # Fetch reviews from the "bookProfile" model
    users = User.objects.all()
    context = {'reviews': reviews,
               'users': users}
    return render(request, 'adminprofile.html', context)

def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            # Create a new Book instance with the form data
            new_book = form.save()
            return HttpResponseRedirect(reverse('bv_overseer:bv_overseer_view'))
    else:   
        form = AddBookForm()

    return render(request, 'add_book.html', {'form': form})

User = get_user_model()

def delete_review(request, review_id):
    # Get the review to delete
    review = get_object_or_404(Review, id=review_id)
    
    if request.method == 'POST':
        # Delete the review
        review.delete()
        # Redirect back to the admin profile page or another suitable page
        return HttpResponseRedirect(reverse('bv_overseer:bv_overseer_view'))