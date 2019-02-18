from django.shortcuts import render,HttpResponse
from time import gmtime,strftime
from datetime import datetime

def index(request):
    context ={
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    time1 = datetime.now()
    print(time1)
    return render(request,"first_display/index.html",context=context)

# Create your views here.
# from django.shortcuts import render
# from time import gmtime, strftime
    
# def index(request):
#     # context = {
#     #     "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
#     # }
#     return render(request,'appname/index.html')
