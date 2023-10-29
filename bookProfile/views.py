from django.shortcuts import render
from bookProfile.models import Review, Book
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from random import sample

# Create your views here.
def show_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    books = Book.objects.all()
    random_books = sample(list(books), 20)
    reviews = Review.objects.filter(book=book)
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

def get_review_json(request, book_id):
    book = get_object_or_404(Book, pk=book_id) 
    reviews = Review.objects.filter(book=book) 
    return HttpResponse(serializers.serialize('json', reviews))

@csrf_exempt
def add_review_ajax(request):
    if request.method == 'POST':
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        book_id = request.POST.get("book_id")  

        book = get_object_or_404(Book, pk=book_id)  

        new_review = Review(rating=rating, review=review, book=book) 
        new_review.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def show_review_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_review_json_by_id(request, id):
    data = Review.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_review_xml(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_review_xml_by_id(request, id):
    data = Review.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


