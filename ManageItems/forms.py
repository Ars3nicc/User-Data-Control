
from django import forms
from .models import *
 
 
# creating a form
class UserForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = UserData
        # specify fields to be used
        fields = [
            "fname",
            "lname",
            "date_created"
        ]