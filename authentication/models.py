from django.db import models

# Create your models here.
class User(models.Model):
    is_User = models.BooleanField(default=False)
    is_Admin = models.BooleanField(default=False)