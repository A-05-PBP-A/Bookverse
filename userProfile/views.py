from django.shortcuts import render, redirect
from userProfile.forms import UserProfileForm
from userProfile.models import Pengguna
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from userProfile.forms import ChangePasswordForm, bookFavForm
from django.contrib.auth.forms import UserChangeForm
from borrowreturn.models import Borrowing
from userProfile.models import UserHistory, UserFav
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# Create your views here.
@login_required(login_url='authentication:login_user')
def show_user_profile(request):
    borrowed = Borrowing.objects.filter(user=request.user, is_returned = False)
    history = UserHistory.objects.filter(user=request.user)
    favorite = UserFav.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'borrowed': borrowed,
        'history' : history,
        'favorite' : favorite,
    }
    return render(request, "userProfile.html", context)

@login_required(login_url='authentication:login_user')
def show_edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('show_user_profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'editProfile.html', {'form': form})

@csrf_exempt
def add_to_favorites(request, book_id):
    if request.method == 'POST':
        book = UserHistory.objects.get(id=book_id).book

        # Assuming bookFavForm is a ModelForm
        form = bookFavForm(request.POST)
        
        if form.is_valid():
            if not UserFav.objects.filter(user=request.user, book=book).exists():
                favBook = form.save(commit=False)
                favBook.user = request.user
                favBook.book = book
                favBook.book_title = favBook.book.title
                favBook.image_url_l = favBook.book.image_url_l
                favBook.reference_id = favBook.book.pk
                favBook.save()

    return HttpResponse(b"OK", status=200)
      

def get_user_favorite(request):
    items = UserFav.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items))

def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']

            # Check if the old password is correct
            if user.check_password(old_password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)  # Update the session to prevent logout

                    # Redirect to a success page or perform any other desired action
                    return redirect('password_changed_successfully')

    else:
        form = ChangePasswordForm()

    return render(request, 'change_password.html', {'form': form})