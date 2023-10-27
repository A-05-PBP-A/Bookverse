from django.shortcuts import render

# Create your views here.
def show_user_profile(request):
    context = {
        'name': 'Ryan',
    }

    return render(request, "userProfile.html", context)