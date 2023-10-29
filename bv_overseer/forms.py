from django import forms
from bookProfile.models import Book  # Import the Book model

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book  # Associate the form with the Book model
        fields = ['isbn', 'title', 'author', 'publication_year', 'publisher', 'image_url_s', 'image_url_m', 'image_url_l']
        # You can customize the fields as needed

    # You can add additional form validation or customization here if required
