from django.db import models
from datetime import date
from .utils import custom_id
from django.contrib.auth.forms import UserCreationForm


class Authentication(models.Model):
    uname = models.CharField(max_length=50, verbose_name='Enter Username'),
    password = models.CharField(max_length=50, verbose_name='Enter Password')
    def __str__(self):
        return self.username

class UserData(models.Model):
    CATEGORY_CHOICES = [
        ('Admin', 'Admin'),
        ('Student', 'Student'),
        ('Teacher', 'Teacher')
    ]
    custom_id = models.CharField(primary_key=True, max_length=11, unique=True, default=custom_id),
    fname = models.CharField(max_length=50, verbose_name='First Name')
    lname = models.CharField(max_length=50, verbose_name='Last Name')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=  True)
    date_created = models.DateField(default=date.today)
    
    def __str__(self):  
        return self.lname
