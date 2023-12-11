from django.forms import ModelForm, FileInput
from django import forms
from django.contrib.auth.models import User
from userProfile.models import UserHistory,UserFav, ProfileDetails

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class UserProfileDetailsForm(forms.ModelForm):
    image = forms.ImageField(widget=FileInput, required=False)
    #widget FileInput agar tidak muncul pesan currently, clear, change saat menampilkan image dengan get
    class Meta:
        model = ProfileDetails
        fields = ['bio', 'image']

class bookHistoryForm(forms.ModelForm):
    class Meta:
        model = UserHistory
        fields = []

class bookFavForm(forms.ModelForm):
    class Meta:
        model = UserFav
        fields = []

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)