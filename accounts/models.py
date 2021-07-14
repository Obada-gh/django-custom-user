from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    USERNAME_FIELD = 'email'
    email = models.EmailField(('email address'), unique=True) # changes email to unique and blank to false
    REQUIRED_FIELDS = ['username'] # removes email from REQUIRED_FIELDS

    def __str__(self):
        return self.username

# Create your models here.
