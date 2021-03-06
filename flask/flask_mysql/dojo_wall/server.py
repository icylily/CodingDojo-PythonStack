from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "keep secret"
bcrypt =  Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^.{2,}')
MESSAGE_REGEX = re.compile(r'^.{5,}')
#regex of password. must have at least one number and one Capital letter. less than 12 characters
# PASS_REGEX = re.compile(r'^(?:(?=.*[A-Z])(?=.*[0-9])).{2,12}$')
PASS_REGEX = re.compile(r'^.{8,}')

@app.route('/')
def index():
    # session['danger'] record whether the user is trying to access informations that does not belong to him.
    # 0 means nothing illegal
    # 1 indicates that there is a violation and that requires a warning
    #2 indicates that need to log out this user 
    if not 'danger' in session:
        session['danger'] = 0
    return render_template("index.html")

#when user sign up ,call this route
@app.route('/process/add', methods=["post"])
def add_user():
    # print(request.form)
    is_valid = True
    #Verify that the form input is valid
    # if len(request.form['form-first-name'])<1:
    if not NAME_REGEX.match(request.form['form-first-name']):
        is_valid = False
        # print("first name is invalid,at least 2 characters")
        flash("first name is invalid,at least 2 characters", 'firstname_signup')
    # if len(request.form['form-last-name']) < 1:
    if not NAME_REGEX.match(request.form['form-last-name']):
        is_valid = False
        # print("last name is invalid,at least 2 characters")
        flash("last name is invalid,at least 2 characters", 'lastname_signup')
    if not EMAIL_REGEX.match(request.form['form-email']):
        is_valid = False
        # print("email is invalid")
        flash("Invalid email address!", 'email_signup')
    if not PASS_REGEX.match(request.form['form-password']):
        is_valid = False
        # print('password is  invalid')
        flash("Passwords must contain at least 8 characters",'password_signup')
    elif (request.form['form-password'] != request.form['form-con-password']):
        is_valid = False
        # print("password doesn't match")
        flash("Password doesn't match ", 'password_signup')
    #if data unvalid ,then return to index. show err messages
    if is_valid == False: 
        return redirect('/')

    #if input all valid ,search table determine whether the email address exist
    mysql = connectToMySQL("dojo_wall")
    pw_hash = bcrypt.generate_password_hash(request.form['form-password'])
    data={
        'fm': request.form['form-first-name'],
        'lm': request.form['form-last-name'],
        'em': request.form['form-email'],
        'pw': pw_hash,
        "am": request.form['form-about-yourself']
    }

    query = "SELECT * FROM tb_user WHERE email = %(em)s"

    result = mysql.query_db(query, data)
    #Determine whether the account exists
    if len(result) != 0:
        is_valid = False
        flash("Email address already existed.", 'email_signup')
    if is_valid == False: 
        return redirect('/')
    #if data all valided, add new user to database , then redirect to login wall page.
    mysql = connectToMySQL("dojo_wall")
    # pw_hash = bcrypt.generate_password_hash(request.form['form-password'])
    query = "INSERT INTO tb_user (first_name,last_name,email,password,about_me) VALUES(%(fm)s,%(lm)s,%(em)s,%(pw)s,%(am)s)"
    # print("pw_hash is",pw_hash)
    # print("query is",query)

    new_user = mysql.query_db(query,data)

    # user loged in .set session 
    session['userid'] = new_user
    session['username'] = request.form['form-first-name'] + \
        ' '+request.form['form-last-name']
    path = '/wall/' + str(new_user)
    return redirect(path)

#session 'username' stored the name only for display welcome setence. userid for search and display user details.
@app.route("/wall/<user>")
def login_success(user):
    if  ('userid'in session) and (session["userid"] != int(user)):
        session["danger"] +=1
        # print('danger is', session["danger"])
        return redirect("/danger")
    if 'username' in session:
        mysql= connectToMySQL('dojo_wall')
        # SELECT first_name as owner_name, tb_message.message from tb_user inner join  tb_message on tb_user.id_user = tb_message.owner_id where receiver_id = 11
        query = "SELECT first_name as owner_name, tb_message.message,tb_message.id_message from tb_user inner join  tb_message on tb_user.id_user = tb_message.owner_id where receiver_id =" + user + ";"
        message_list = mysql.query_db(query)
        # print(message_list)
        session["count_message"] = len(message_list)
        mysql = connectToMySQL('dojo_wall')
        query = "SELECT COUNT(*) AS count FROM tb_message WHERE owner_id = " + \
            user + ";"
        sent_message = mysql.query_db(query)
        # print("seent_message is :",sent_message)
        session["sent_message"]=sent_message[0]["count"]
        mysql= connectToMySQL('dojo_wall')
        query = "SELECT first_name as receiver,id_user from tb_user where id_user !=" +\
            user +";"
        receiver_list = mysql.query_db(query)
        # print(receiver_list)
        return render_template('wall.html',message_list=message_list,receiver_list=receiver_list)
    else:
        session["danger"] = 0
        return render_template('wall.html')


@app.route('/logout')
def logout():

    session.clear()
    return redirect('/')


@app.route('/precess/login',methods=['post'])
def login():
    #first, data validation
    is_valid = True
    if not EMAIL_REGEX.match(request.form['form-email']):
        is_valid = False
        # print("email is invalid")
        flash("Please input a valid email address!", 'email_login')
    if not PASS_REGEX.match(request.form['form-password']):
        is_valid = False
        # print('password is  invalid')
        flash("Passwords must contain at least one uppercase letter and one number", 'password_login')
    #if data unvalid ,then return to index. show err messages
    if is_valid == False:
        return redirect('/')
    #if data all valided, add new user to database , then redirect to wall page.
    
    mysql = connectToMySQL("dojo_wall")
    pw_hash = bcrypt.generate_password_hash(request.form['form-password'])
    data = {
        'em': request.form['form-email'],
        'pw': pw_hash,
    }
    query = "SELECT * FROM tb_user WHERE email = %(em)s"

    login_user = mysql.query_db(query, data)
    #Determine whether the account exists
    if len(login_user)==0:
        is_valid = False
        flash("Email address doesn't exist.Please input another email.", 'email_login')
    elif len(login_user)>1:
        is_valid = False
        flash("Something Wrong.This email duplicated registered.Please contact admin.", 'email_login')
    #if email not exist or duplicated , redirect to index and show err, don't need to check pass
    if is_valid == False:
        return redirect('/')
    
    #all righg ,check pass
    if bcrypt.check_password_hash(login_user[0]['password'], request.form['form-password']):
        session['username'] = login_user[0]['first_name'] + \
            ' '+login_user[0]['last_name']
        session["userid"] = login_user[0]['id_user']
        path = '/wall/' + str(login_user[0]['id_user'])
        return redirect(path)
    else:
        is_valid = False
        # print('password is  invalid')
        flash("Wrong password. Please enter the correct password", 'password_login')
        return redirect('/')

# post message
@app.route('/message/send',methods=['post'])
def send_message():
    # print(request.form)
    if not MESSAGE_REGEX.match(request.form['message']):
        # is_valid = False
        # print("first name is invalid,at least 2 characters")
        flash("message is invalid,at least 5 characters", 'message')
        path="/wall/" + str(session['userid'])
        return redirect(path)
    mysql=connectToMySQL("dojo_wall")
    data={
        "ow":str(session["userid"]),
        "re":request.form["receiver_id"],
        "me":request.form["message"]
    }
    quere = "INSERT INTO tb_message (owner_id,receiver_id,message) VALUES(%(ow)s,%(re)s,%(me)s);"
    new_message = mysql.query_db(quere,data)
    path = '/wall/' + str(session["userid"])
    return redirect(path)




#delete message
@app.route('/wall/delete/<message_id>')
def delete_message(message_id):
    mysql = connectToMySQL("dojo_wall")
    data = {
        "md": message_id
    }
    query = "SELECT owner_id FROM tb_message WHERE id_message = %(md)s"
    owner_id = mysql.query_db(query, data)
    # print("owner_id[0]['owner_id']", owner_id)
    if ('userid'in session) and (session["userid"] != owner_id[0]['owner_id']):
        session["danger"] += 1
        # print('danger is', session["danger"])
        return redirect("/danger")
    mysql=connectToMySQL("dojo_wall")
    query = "DELETE FROM tb_message WHERE id_message = %(md)s"
    
    mysql.query_db(query,data)
    path = '/wall/' + str(session["userid"])
    return redirect(path)



@app.route('/danger')
def danger():
    if session["danger"] ==1 :
        flash("You are tring to accesss some informations that does not belong to you. Next time you attemp an activity like this we'll log you off authmatically.", 'danger')
        return render_template("warning.html")
    if session["danger"] >1:
        if 'userid' in session:
            session.pop("userid")
        if 'username' in session:
            session.pop("username")
        session["danger"] = 0
        flash("You were being forcibly logged off", 'danger')
        return render_template("warning.html")
    



    

if __name__ == "__main__":
    app.run(debug=True)
