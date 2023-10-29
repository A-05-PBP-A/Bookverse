from django.shortcuts import render, redirect
from userProfile.forms import UserProfileForm
from userProfile.models import Pengguna
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from userProfile.forms import ChangePasswordForm
from django.contrib.auth.forms import UserChangeForm


# Create your views here.
@login_required(login_url='authentication:login_user')
def show_user_profile(request):
    context = {
        'name': request.user.username,
    }

    return render(request, "userProfile.html", context)

def show_edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'editProfile.html', {'form': form})

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