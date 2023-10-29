from django.db import models
from datetime import date

# Create your models here.
class Main(models.Model):
    current_date = models.DateField(default=date.today)