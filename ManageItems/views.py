from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .forms import NewUserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .models import *
from .forms import *


def main(request):
    total= UserData.objects.count()
    teachers = UserData.objects.filter(category='Teacher').count()
    students = UserData.objects.filter(category='Student').count()
    return render(request,'main.html', {'total': total, 'teachers':teachers, 'students':students})


def aboutus(request):
    return HttpResponse('Page Not Found', status=404)

def usertable(request):
    total= UserData.objects.count()
    user = UserData.objects.all()
    return render(request,'views/usertable.html', {'user': user, 'total': total})

def student_table(request):
    student = UserData.objects.filter(category='Student').all()

    return render(request,'views/student_table.html', {'student': student})

def teacher_table(request):
    teacher = UserData.objects.filter(category='Teacher').all()

    return render(request,'views/teacher_table.html', {'teacher': teacher})

# def login_usere(request):
#     if request.method == 'POST':
#         # Process the request if posted data are available
#         username = request.POST['username']   
#         password = request.POST['password']
#         # Check username and password combination if correct
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             # Save session as cookie to login the user
#             login(request, user)
#             # Success, now let's login the user.
#             return render(request, 'index.html')
#     else:
#         # No post data availabe, let's just show the page to the user.
#         return render(request, 'login.html')
# CRUD OPERATION VIEWS --------------------------------
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    user = UserData.objects.all()
 
    # add the dictionary during initialization
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/usertable")
    context['form']= form
    return render(request, "views/create_user.html", context)

def detail_view(request, id):
    context ={}

    context["user"] = UserData.objects.get(id = id)
          
    return render(request, "views/detail_view.html", context)
 
# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    user = UserData.objects.all()
    obj = get_object_or_404(UserData, id = id)
 
    # pass the object as instance in form
    form = UserForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/usertable")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "views/update_user.html", context)

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
        return HttpResponseRedirect("/usertable")
 
    return render(request, "views/delete_user.html", context)
#  ------------------------------------------------------------------
# JSON View
def json_view(request):
    data=list(UserData.objects.values())
    return JsonResponse(data,safe=False)
