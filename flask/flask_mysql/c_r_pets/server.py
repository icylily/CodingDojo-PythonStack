from flask import Flask, render_template,redirect,request
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL("pets")
    allpets = mysql.query_db("SELECT * FROM pets;")
    print(allpets)
    return render_template("index.html", pets=allpets)

@app.route('/addpet',methods=['post'])
def addpet():
    mysql = connectToMySQL("pets")
    query = "INSERT INTO pets(name,type,created_at,updated_at) VALUES (%(pm)s,%(pt)s, NOW(),NOW())"
    data = {
        "pm":request.form["petname"],
        "pt":request.form["pettype"]
    }
    newpet_id = mysql.query_db(query,data)
    print(newpet_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
