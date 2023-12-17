from django import forms
from bookProfile.models import Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'author', 'publication_year', 'publisher', 'image_url_s', 'image_url_m', 'image_url_l']

    widgets = {
        'isbn': forms.TextInput(attrs={'size': 50}),
        'title': forms.TextInput(attrs={'size': 50}),
        'author': forms.TextInput(attrs={'size': 50}),
        'publication_year': forms.TextInput(attrs={'size': 4}),
        'publisher': forms.TextInput(attrs={'size': 50}),
        'image_url_s': forms.TextInput(attrs={'size': 50}),
        'image_url_m': forms.TextInput(attrs={'size': 50}),
        'image_url_l': forms.TextInput(attrs={'size': 50}),
    }

class DeleteBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = []