from django.shortcuts import render
from django.http import HttpResponseNotFound
from bookProfile.models import Review
import requests

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