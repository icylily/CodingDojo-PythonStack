from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    buying_strawberry = request.form['strawberry']
    buying_blackberry = request.form['blackberry']
    buying_apple = request.form['apple']
    buying_raspberry = request.form['raspberry']
    total_fruit = int(buying_strawberry)+int(buying_blackberry)+int(buying_apple)+int(buying_raspberry)
    firstname = request.form['first_name']
    lastname = request.form['last_name']
    studentid = request.form['student_id']
    return render_template("checkout.html", strawberry=buying_strawberry, blackberry=buying_blackberry, apple=buying_apple,
     raspberry=buying_raspberry,firstname = firstname,lastname = lastname, studentid=studentid,total=total_fruit)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
