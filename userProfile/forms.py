from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from userProfile.models import Pengguna

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Pengguna
        fields = ['bio']

    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.bio = self.cleaned_data['bio']
        if commit:
            user.save()
        return user

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)