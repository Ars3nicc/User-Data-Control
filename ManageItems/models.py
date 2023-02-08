from django.db import models

class UserData(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.lname
