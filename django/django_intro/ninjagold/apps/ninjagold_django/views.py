from django.shortcuts import render,HttpResponse,redirect
import random
import datetime
def index(request):
    # return HttpResponse("we are here ,ninja gold")
    if not ('gold' in request.session):
        request.session['gold'] = 0
        request.session['log'] = ""
        request.session['steps']= 20
        request.session['goal'] = 200
        request.session['current_steps'] = 0
        request.session['status'] = 0 # initial status
        # request.session['color'] = "abd<span class='red'>bac</span>"
    return render(request, "ninjagold_django/index.html")

# Create your views here.

def process_money(request):
    # if request.method == "POST":
    #     print("getting post !")

    # return redirect('/')
    
    if request.POST['wich_place'] == 'farm':
        increase = random.randint(10, 20)
    elif request.POST['wich_place'] == 'cave':
        increase = random.randint(5, 10)
    elif request.POST['wich_place'] == 'house':
        increase = random.randint(2, 5)
    elif request.POST['wich_place'] == 'casino':
        increase = random.randint(-50, 50)

    request.session['gold'] += increase
    # session['log'] = 'good job!'
    if increase < 0:
        log_str = "<span class='red'>Entered a casino and lost " + \
            str(0-increase) + 'golds...Ouch..'
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        log_str += otherStyleTime + "</span>"

    else:
        log_str = 'Earned ' + str(increase) + 'golds from ' + \
            request.POST['wich_place'] + '!'
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        log_str += otherStyleTime

    request.session['log'] = log_str + "<br>" + "\r" + request.session['log']
    # session['log'] = "get reward /n" + session['log']request.
    request.session['current_steps'] +=1
    if ((request.session['current_steps'] <= request.session['steps']) and request.session['gold']>=request.session['goal']):
        request.session['status'] = 1  # won
    elif request.session['current_steps'] >= request.session['steps']:
        request.session['status'] = 2 #fail
    return redirect('/')



def refresh(request):
    # for key in request.session.keys():
    #     del request.session[key]
    del request.session['gold']
    del request.session['log']
    # del request.session['current_steps']
    # del request.sesssion['status']

    return redirect('/')
