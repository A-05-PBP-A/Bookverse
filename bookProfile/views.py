from django.shortcuts import render
from bookProfile.models import Review, Book
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def show_profile(request):
    context = {
    }

    return render(request, "profile.html", context)

def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json",data), content_type="application/json")