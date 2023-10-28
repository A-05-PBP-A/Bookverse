from django.shortcuts import render

# Create your views here.
def show_overseer_main(request):
    context = {
        'name': 'Pak Bepe',
    }

    return render(request, "adminprofile.html", context)