from django.forms import ModelForm
from django import forms
from borrowreturn.models import Borrowing
from bookProfile.models import Book
from django.utils.text import Truncator

class TruncatedLabelModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return Truncator(obj.title).chars(50)
    
class BorrowingForm(ModelForm):
    class Meta:
        model = Borrowing
        fields = []
