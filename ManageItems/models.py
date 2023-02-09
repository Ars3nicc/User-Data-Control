from django.db import models
from datetime import date

class UserData(models.Model):
    fname = models.CharField(max_length=50, verbose_name='First Name')
    lname = models.CharField(max_length=50, verbose_name='Last Name')
    date_created = models.DateField(default=date.today)
    
    def __str__(self):  
        return self.lname
