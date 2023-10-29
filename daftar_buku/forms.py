from django.forms import ModelForm
from daftar_buku.models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "feeds", "rate"]