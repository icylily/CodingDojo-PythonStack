from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.

def index(request):

    return render(request,"login_app/index.html")

def process_register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
            print(messages)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        this_first_name = request.POST["first_name"]
        this_last_name  = request.POST["last_name"]
        this_email = request.POST["email"]
        this_password = bcrypt.hashpw(
            request.POST["password"].encode(), bcrypt.gensalt())
        # this_password = request.POST["password"]
        this_user = User.objects.create(first_name=this_first_name,last_name = this_last_name,email=this_email,password=this_password)
        print(this_user.id,this_user.first_name)
       #set session
        return redirect("/success")

    # return HttpResponse("registration")
def process_login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
            print(messages)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        #set session
        request.session["logined"] = "yes"
        user = User.objects.filter(email=request.POST["email"])
        request.session["first_name"] = user[0].first_name
        request.session["last_name"] = user[0].last_name
        # request.session["logined_user"] = User.objects.filter(
        #     email=request.POST["email"])
        return redirect("/success")
    
def success(request):

    return render(request,"login_app/success.html")

def logout(request):
    del request.session["logined"]
    del request.session["first_name"]
    del request.session["last_name"]
    return redirect('/')
