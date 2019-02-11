from flask import Flask,render_template, request, redirect,session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'set a secretd key'

@app.route('/')
def index():
    if not('gold' in session):
        session['gold'] = 0
        session['log'] = ""
        session['color'] = "abd<span class='red'>bac</span>"
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['wich_place'] == 'farm':
        increase = random.randint(10,20)
    elif request.form['wich_place'] == 'cave':
        increase = random.randint(5, 10)
    elif request.form['wich_place'] == 'house':
        increase = random.randint(2, 5)
    elif request.form['wich_place'] == 'casino':
        increase = random.randint(-50, 50)
    
    session['gold'] += increase
    # session['log'] = 'good job!'
    if increase < 0 :
        log_str = "<span class='red'>Entered a casino and lost " + str(0-increase) + 'golds...Ouch..' 
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        log_str += otherStyleTime + "</span>" 

    else:
        log_str = 'Earned ' + str(increase) + 'golds from ' + \
            request.form['wich_place'] +'!'
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        log_str += otherStyleTime

    session['log'] = log_str + "<br>" +"\r"+ session['log']
    # session['log'] = "get reward /n" + session['log']

    return redirect('/')
@app.route('/refresh',methods=['POST'])
def refresh():
    session.clear()
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)
