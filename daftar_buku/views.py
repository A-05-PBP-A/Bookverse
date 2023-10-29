from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core import serializers
from django.urls import reverse
from daftar_buku.forms import FeedbackForm

from daftar_buku.models import Main, Feedback
from bookProfile.models import Book

from django.utils import timezone

book = Book.objects.all()

def show_main(request):
    date = Main.objects.all()
    feedback = Feedback.objects.all()
    context = {
        'buku' : book,
        'tanggal' : date,
        'feedback' : feedback,
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

def feedback_form(request):
    form = FeedbackForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('daftar_buku:show_main'))

    context = {'form': form}
    return render(request, "feedback_form.html", context)

def show_feedback_json(request):
    feedback = Feedback.objects.all()
    return HttpResponse(serializers.serialize("json", feedback), content_type="application/json")
