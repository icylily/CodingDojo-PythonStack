
###users####
from django.shortcuts import render, HttpResponse, redirect
# from django.core.urlresolvers import reverse
from django.urls import reverse
# Create your views here.


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs ")

def register(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to log in")

def new_user(request):
    print("hello, I am your first request")
    return redirect(reverse('my_new'))
def all_users(request):
    return HttpResponse("placeholder to later display all the list of users")
