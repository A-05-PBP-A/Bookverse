from django.shortcuts import render
from bookProfile.models import Review
from django.shortcuts import render, redirect
from .forms import AddBookForm
from django.urls import reverse

# Create your views here.
def show_overseer_main(request):
    context = {
        'name': 'Pak Bepe',
    }

    return render(request, "adminprofile.html", context)

def bv_overseer_view(request):
    reviews = Review.objects.all()  # Fetch reviews from the "bookProfile" model
    context = {'reviews': reviews}
    return render(request, 'adminprofile.html', context)

def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            # Create a new Book instance with the form data
            new_book = form.save()
            return redirect(reverse('bv_overseer: bv_overseer_view'))
    else:   
        form = AddBookForm()

    return render(request, 'add_book.html', {'form': form})