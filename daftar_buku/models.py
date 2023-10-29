from django.db import models
from datetime import date

# Create your models here.
class Main(models.Model):
    current_date = models.DateField(default=date.today)

class Feedback(models.Model):
    RATE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    name = models.CharField(max_length=255)
    feeds = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)