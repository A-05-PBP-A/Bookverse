import json
from django.shortcuts import render, redirect, get_object_or_404
from userProfile.forms import UserProfileForm, UserProfileDetailsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from userProfile.forms import ChangePasswordForm, bookFavForm
from borrowreturn.models import Borrowing
from userProfile.models import UserHistory, UserFav, ProfileDetails
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from bookProfile.models import Book
from django.contrib.auth.models import User


# Create your views here.
def show_user_profile(request):
    # Check if ProfileDetails instance exists for the current user
    profile_details_queryset = ProfileDetails.objects.filter(user=request.user)

    if profile_details_queryset.exists():
        profile_details = profile_details_queryset.last()  # Use the last instance
    else:
        # Create a new ProfileDetails instance if none exists
        profile_details = ProfileDetails.objects.create(user=request.user)

    borrowed = Borrowing.objects.filter(user=request.user, is_returned=False)
    history = UserHistory.objects.filter(user=request.user)
    favorite = UserFav.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'borrowed': borrowed,
        'history': history,
        'favorite': favorite,
        'bio': profile_details.bio,
        'image': profile_details.image.url if profile_details.image else None,
    }
    return render(request, "userProfile.html", context)

@login_required(login_url='authentication:login_user')
def edit_profile(request):
    user_instance = request.user
    profile_details_instances = ProfileDetails.objects.filter(user=user_instance)

    # Choose the last instance if it exists, otherwise create a new one
    profile_details_instance = profile_details_instances.last() or ProfileDetails.objects.create(user=user_instance)

    if request.method == 'POST':
        formUser = UserProfileForm(request.POST, instance=user_instance)
        formProfileDetails = UserProfileDetailsForm(request.POST, request.FILES, instance=profile_details_instance)

        if 'remove_profile_picture' in request.POST:
            # Handle removing profile picture
            profile_details_instance.image = None
            profile_details_instance.save()
            # auto refresh in the same page
            return redirect('userProfile:edit_profile')

        if 'remove_bio' in request.POST:
            # Handle almost removing bio
            profile_details_instance.bio = ''
            profile_details_instance.save()
            # auto refresh in the same page
            return redirect('userProfile:edit_profile')

        if formUser.is_valid() and formProfileDetails.is_valid():
            user_data_changed = formUser.data != formUser.initial

            if user_data_changed:
                formUser.save()

            profile_details_instance.bio = formProfileDetails.cleaned_data['bio']
            # Kalau user sudah upload profile picture
            if profile_details_instance.image is not None:
                profile_details_instance.image = formProfileDetails.cleaned_data['image']
            profile_details_instance.save()

            # in django is different from regular python the two if must be met to save changes
            return redirect('userProfile:show_user_profile')

    else:
        formUser = UserProfileForm(instance=user_instance)
        formProfileDetails = UserProfileDetailsForm(instance=profile_details_instance)
        

    context = {
        'formUser': formUser,
        'formProfileDetails': formProfileDetails,
        'image': profile_details_instance.image.url if profile_details_instance.image else None,
    }

    return render(request, 'editProfile.html', context)

@csrf_exempt
def add_to_favorites(request, book_id):
    if request.method == 'POST':
        book = UserHistory.objects.get(id=book_id).book
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

@csrf_exempt
def add_to_favorites_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bookId = data['bookId']

        existing_favorite = existing_favorite = UserFav.objects.filter(user=request.user, book__id=bookId)
        if existing_favorite.exists():
            existing_favorite = UserFav.objects.filter(user=request.user, book__id=bookId).last()
            if existing_favorite:
                # Book already exists in favorites
                return JsonResponse({"status": "error", "message": "Book already in favorites"}, status=400)
            
        fav_book = Book.objects.get(id=bookId)

        new_fav_book = UserFav.objects.create(
            user = request.user,
            book = fav_book,
            book_title = fav_book.title,
            image_url_l = fav_book.image_url_l,
            reference_id = bookId,
        )

        new_fav_book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def delete_book(request, book_id):
    if request.method == 'POST':
        # Perform the book deletion in the UserFav model
        fav_book = Book.objects.get(id=book_id)
        user_fav = UserFav.objects.get(book=fav_book)  # Assuming you have authentication
        user_fav.delete()
        return JsonResponse({'message': 'Book deleted successfully'})
    else:
        return JsonResponse({'message': 'Failed to delete book'}, status=400)
      

def get_user_favorite(request):
    items = UserFav.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items), content_type="application/json")

def get_user_favorite_flutter(request, username):
    user = User.objects.get(username=username)
    items = UserFav.objects.filter(user=user)
    return HttpResponse(serializers.serialize('json', items), content_type="application/json")

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

    return render(request, 'changePassword.html', {'form': form})