### random_word ###

from django.shortcuts import render,HttpResponse,redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    # return HttpResponse("random word")
    context={
        "ran_str": get_random_string(length=14)
    }
    if not ('attmpts' in request.session):
        request.session['attmpts'] = 1
    else:
        request.session['attmpts']+=1
    print("request.session['attmpts']", request.session['attmpts'])
        
    # print(context)
    if request.method == "POST":
        if request.POST["submit"] == "Reset":
            del request.session['attmpts']
            return redirect('/random_word')
    return render(request,"random_word/random_word.html",context = context)
