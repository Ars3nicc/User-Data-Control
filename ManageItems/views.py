from django.shortcuts import render

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .models import *
from .forms import *

# Create your views here.
def main(request):
    return render(request,'index.html')


def aboutus(request):
    return render(request,'aboutus.html')

def usertable(request):
    user = UserData.objects.all()
    return render(request,'usertable.html', {'user': user})

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_user.html", context)

def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["user"] = UserData.objects.get(id = id)
          
    return render(request, "detail_view.html", context)
 
# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(UserData, id = id)
 
    # pass the object as instance in form
    form = UserForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_user.html", context)

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(UserData, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("")
 
    return render(request, "delete_user.html", context)