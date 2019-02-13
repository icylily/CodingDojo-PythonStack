from flask import Flask, render_template,redirect,request
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def all_users():
    mysql = connectToMySQL('usersdb')
    users = mysql.query_db("SELECT * FROM users;")
    print(users)
    return render_template("all_users.html",allusers=users)
@app.route('/users/new')
def add_user():

    return render_template("add_user.html")
@app.route('/user/add',methods=['post'])
def add_user_excute():
    mysql = connectToMySQL('usersdb')
    query = "INSERT INTO users(first_name,last_name,email,created_at,updated_at) VALUES (%(fm)s,%(lm)s,%(em)s, NOW(),NOW())"
    data = {
        "fm": request.form["firstname"],
        "lm":request.form["lastname"],
        "em":request.form["email"]
    }
    newuserid = mysql.query_db(query,data)
    print(newuserid)
    path = '/users/'+str(newuserid)
    return redirect(path)

@app.route('/users/<userid>')
def show_one_user(userid):
    mysql = connectToMySQL('usersdb')
    query = "SELECT * FROM users where user_id =" + userid

    user = mysql.query_db(query)
    print(user)
    return render_template('one_user.html',user=user)


@app.route("/users/<userid>/edit")
def edit_user(userid):
    mysql = connectToMySQL('usersdb')
    query = "SELECT * FROM users where user_id =" + userid

    user = mysql.query_db(query)
    return render_template("edit_users.html",user=user)


@app.route("/users/<userid>/edit/excute", methods=['post'])
def edit_user_excute(userid):
    mysql = connectToMySQL('usersdb')
    query = "UPDATE users SET first_name =%(fm)s,last_name=%(lm)s,email=%(em)s,updated_at=NOW() where user_id= " +userid +';'
    data = {
        "id": userid,
        "fm": request.form["firstname"],
        "lm": request.form["lastname"],
        "em": request.form["email"]
    }
    user = mysql.query_db(query,data)
    print(user)
    path = '/users/'+str(userid)
    return redirect(path)


@app.route("/users/<userid>/delete")
def delete_user(userid):
    mysql = connectToMySQL('usersdb')
    query = "DELETE FROM users where user_id =" + userid

    user = mysql.query_db(query)
    print(user)
    return redirect("/users")
if __name__=="__main__":
    app.run(debug=True)
