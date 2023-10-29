from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers

from daftar_buku.models import Main
from bookProfile.models import Book

book = Book.objects.all()

def show_main(request):
    date = Main.objects.all()
    #book = Book.objects.all()
    context = {
        'buku' : book,
        'tanggal' : date,
    }

    return render(request, "landing_page.html", context)

def get_books_json(request):
    #book = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book))

def filter_books(request):
    keyword = request.GET.get('keyword', '')
    filter_type = request.GET.get('filter_type', '')

    if filter_type == 'title':
        #filtered_books = Book.objects.filter(title__icontains=keyword)
        filtered_books = book.filter(title__icontains=keyword)
    elif filter_type == 'author':
        #filtered_books = Book.objects.filter(author__icontains=keyword)
        filtered_books = book.filter(author__icontains=keyword)
    elif filter_type == 'publication_year':
        #filtered_books = Book.objects.filter(publication_year__icontains=keyword)
        filtered_books = book.filter(publication_year__icontains=keyword)
    elif filter_type == 'publisher':
        #filtered_books = Book.objects.filter(publisher__icontains=keyword)
        filtered_books = book.filter(publisher__icontains=keyword)
    else:
        #filtered_books = Book.objects.all()
        filtered_books = book

    return HttpResponse(serializers.serialize('json', filtered_books))
    #return JsonResponse(filtered_books, safe=False)
    #data = [{'image_url_l': book.image_url_l, 'title': book.title, 'author': book.author, 'publication_year': book.publication_year, 'publisher': book.publisher} for book in filtered_books]
    #return JsonResponse(data, safe=False)