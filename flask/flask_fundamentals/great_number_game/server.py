from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret'

@app.route('/')
def index():
    if not('value' in session):
        session['value']= random.randint(1,100)
    print(session['value'])
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    print(request.form)
    if request.form['guessed'].isdigit():
        session['guessed'] = int(request.form['guessed'])
        print(session['guessed'])
        if (session['guessed'] < 1 or session['guessed']>100):
            session['result'] = 0   # please input a valid number
        elif(session['guessed'] < session['value']):
            session['result'] = 1   #  low
        elif(session['guessed'] > session['value']):
            session['result'] = 2  # high
        else:
            session['result'] = 3   #right

    else:
        print("not a number!")
        session['result']=0   # please input a valid number

    print(session['result'])
    return redirect('/')

@app.route('/reset',methods=['post'])
def reset():
    session.clear()
    return redirect('/')

if __name__  == '__main__':
    app.run(debug= True)


