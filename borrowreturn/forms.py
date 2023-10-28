from django.forms import ModelForm
from borrowreturn.models import Borrowing

class BorrowingForm(ModelForm):
    class Meta:
        model = Borrowing
        fields = ["name", "price", "description"]