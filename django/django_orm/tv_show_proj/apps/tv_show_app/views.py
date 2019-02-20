from django.shortcuts import render,redirect,HttpResponse
from .models import Show

# Create your views here.
def index(request):
    return redirect('/shows')
def shows(request):

    context={
        "all_shows":Show.objects.all(),
    }
    return render(request,"tv_show_app/all_shows.html",context)
def add_show(request):

    return render(request,"tv_show_app/add_show.html")


def show_detail(request,show_id):
    context={
        "this_show":Show.objects.get(id= int(show_id)),
    }
    return render(request, "tv_show_app/show_detail.html",context)
    # return HttpResponse("this show_details")

def process(request):

    if request.POST['which_place'] == 'add_show':
        this_title = request.POST['title']
        this_desc = request.POST['desc']
        this_release_date = request.POST['release_date']
        this_network = request.POST['network']
        this_show = Show.objects.create(title=this_title, network = this_network,release_date= this_release_date,desc=this_desc)
        print(this_show.id)
        path = 'shows/' + str(this_show.id)
        return redirect(path)
    elif request.POST['which_place'] == 'edit_show':
        this_show = Show.objects.get(id=int(request.POST['show_id']))
        this_show.title=request.POST['title']
        this_show.desc = request.POST['desc']
        this_show.release_date = request.POST['release_date']
        this_show.network = request.POST['network']
        path = 'shows/' + str(request.POST['show_id'])
        return redirect(path)
    else:
        return HttpResponse("wrong")


def edit_show(request,show_id):
    context = {
        "this_show": Show.objects.get(id=int(show_id)),
    }
    return render(request, "tv_show_app/edit_show.html", context)

def destroy(request,show_id):
    this_show = Show.objects.get(id=int(show_id))
    this_show.delete()
    return redirect('/')