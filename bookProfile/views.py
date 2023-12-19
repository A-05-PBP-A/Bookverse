from django.shortcuts import render
from bookProfile.models import Review, Book
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from random import sample
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
@login_required(login_url='/login/')
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

def get_book_by_id(request, book_id):
    data = Book.objects.get(pk=book_id)
    return HttpResponse(serializers.serialize("json",[data]), content_type="application/json")

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
        user = request.user
        name = request.user.username

        book = get_object_or_404(Book, pk=book_id)    

        new_review = Review(rating=rating, review=review, book=book, user=user ,name=name) 
        new_review.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_review_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book_id = int(data["book_id"])

        existing_review = Review.objects.filter(user=request.user, book__id=book_id).first()
        if existing_review:
            return JsonResponse({"status": "error", "message": "You have already reviewed this book"}, status=400)

        new_review = Review.objects.create(
            user=request.user,
            name=request.user.username,
            book=get_object_or_404(Book, pk=book_id),
            rating=int(data["rating"]),
            review=data["review"],
        )

        new_review.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return JsonResponse({"status": "success", "message": "Review deleted successfully"}, status=200)

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


