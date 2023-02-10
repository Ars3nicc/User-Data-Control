from django.contrib import admin
from .models import UserData
# Register your models here.
admin.site.register(UserData)

class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('Last Name', 'pub_date', 'Date Created')