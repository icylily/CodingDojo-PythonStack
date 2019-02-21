
### wall_app.views###
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import *
# from login_app.models import *
from apps.login_app.models import User

# Create your views here.
def index(request):
    if request.session["logined"] == "yes":
        messages = Message.objects.all().order_by("-created_at")
        context = {
            "message_list":messages,
        }
        return render(request,"wall_app/wall.html",context)
    return render(request,"wall_app/wall.html")


def process_post_message(request):
    message_from_form = request.POST["message"]
    print("message is ", message_from_form)
    this_message = Message.objects.create(message =message_from_form, user_id=User.objects.get(
        id=int(request.session["current_user"])))
    print (this_message.id)
    return redirect('/wall')


def process_post_comment(request):
    comment_from_form = request.POST["comment"]
    print("comment is ", comment_from_form)
    this_comment = Comment.objects.create(comment=comment_from_form, user=User.objects.get(id=int(request.session["current_user"])), message=Message.objects.get(id=int(request.POST["message"])))
 
    print("add comment")
    print(this_comment.id)
    return redirect('/wall')
