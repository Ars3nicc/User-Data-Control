from django.db import models

# Create your models here.
class hwItems(models.Model):
    hwItems=models.SmallIntegerField(primary_key=True)
    hwName=models.CharField(max_length=50)
    hwDescription=models.TextField(max_length=200)
    hwQty=models.SmallIntegerField