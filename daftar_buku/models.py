from django.db import models
from django.utils import timezone

# Create your models here.
class Main(models.Model):
    date = models.DateField(default=timezone.now)