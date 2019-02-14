from flask import Flask, render_template,redirect,session,flash,request
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = "keep secret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route("/")
def index():
    return render_template("index.html")


    
@app.route('/process', methods=['POST'])
def submit():
    if not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
        flash("Invalid email address!")
        return redirect('/')
    mysql = connectToMySQL('emails')
    email_address = request.form['email']
    
    query = "INSERT INTO tb_email (email) VALUES (%(em)s);"
    data={
        "em": request.form['email']
    }
    email_id = mysql.query_db(query,data)
    if email_id == False:
        flash("Existed email address!")
        return redirect('/')
    mysql = connectToMySQL('emails')
    email_list = mysql.query_db("SELECT * FROM tb_email;")

    return render_template("show_emails.html", added_email=email_address,emails=email_list)


@app.route("/process/<id>/delete")
def delete_user(id):
    mysql = connectToMySQL('emails')
    query = "DELETE FROM tb_email where id =" + id

    delete = mysql.query_db(query)
    print(delete)
    mysql = connectToMySQL('emails')
    email_list = mysql.query_db("SELECT * FROM tb_email;")

    return render_template("show_emails.html", deleted="deleted",emails=email_list)


if __name__ == "__main__":
    app.run(debug=True)
