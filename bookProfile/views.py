from django.shortcuts import render
from bookProfile.models import Review, Book
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from random import sample

# Create your views here.
def show_review(request):
    reviews = Review.objects.all()
    books = Book.objects.all()
    random_books = sample(list(books), 7)
    book = get_object_or_404(Book, pk=1)
    context = {
        'reviews' : reviews,
        'books' : books,
        'book' : book,
        'random_books' : random_books,
    }

    return render(request, "profile.html", context)

def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json",data), content_type="application/json")

def get_review_json(request):
    review = Review.objects.all()
    return HttpResponse(serializers.serialize('json', review))

@csrf_exempt
def add_review_ajax(request):
    if request.method == 'POST':
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        # user = request.user

        new_review = Review(rating=rating, review=review)
        new_review.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def show_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")