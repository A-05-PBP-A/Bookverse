from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers

from daftar_buku.models import Main
from bookProfile.models import Book

from django.utils import timezone

book = Book.objects.all()

def show_main(request):
    tanggal = Main.objects.all()
    context = {
        'buku' : book,
        'tanggal' : tanggal,
    }

    return render(request, "landing_page.html", context)

def get_books_json(request):
    return HttpResponse(serializers.serialize('json', book))

def filter_books(request):
    keyword = request.GET.get('keyword', '')
    filter_type = request.GET.get('filter_type', '')

    if filter_type == 'title':
        filtered_books = book.filter(title__icontains=keyword)
    elif filter_type == 'author':
        filtered_books = book.filter(author__icontains=keyword)
    elif filter_type == 'publication_year':
        filtered_books = book.filter(publication_year__icontains=keyword)
    elif filter_type == 'publisher':
        filtered_books = book.filter(publisher__icontains=keyword)
    else:
        filtered_books = book

    return HttpResponse(serializers.serialize('json', filtered_books))