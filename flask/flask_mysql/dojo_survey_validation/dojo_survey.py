from flask import Flask,render_template,redirect,request,flash,session
from mysqlconnection import connectToMySQL
import string

app = Flask(__name__)
app.secret_key ="keep it as a secret"

@app.route('/')
def index():
    mysql = connectToMySQL('user_survey')
    background = mysql.query_db("SELECT * FROM backgroud;")
    mysql = connectToMySQL('user_survey')
    language = mysql.query_db("SELECT * FROM language;")
    mysql = connectToMySQL('user_survey')
    location = mysql.query_db("SELECT * FROM location;")
    mysql = connectToMySQL('user_survey')
    source = mysql.query_db("SELECT * FROM source;")
    return render_template("index.html",background= background,language = language,location=location,source=source)

@app.route('/results',methods= ['GET', 'POST'])
def show_results():
    is_valid = True
    # data validating
    if len(request.form['name']) < 1:
    	is_valid = False
    	flash("Please enter a name")
    if  len(request.form.getlist('source'))<1:
    	is_valid = False
    	flash("Please choose at least one of source")
    if len(request.form.get('comments')) >148: #\r\n used 18 characters.
    	is_valid = False
    	flash("Comments should not exceed 120 characters")
    #if there have some unavaliable data then redirect to index and show the flash messages
    if is_valid ==False:
        return redirect('/')
    #if all data are avaliable , inserto record to table and redirect to show this record
    if is_valid == True:
        data = {
            "name": request.form['name'],
            "lc": request.form['location'],
            "la": request.form['languge'],
            "ba": request.form['background'],
            "cm": request.form['comments'],
            "sr": request.form.getlist('source')
        }
        print(request.form.getlist('source'))
        
        mysql = connectToMySQL('user_survey')

        query = "INSERT INTO survey(`username`, `location_id`, `language_id`, `background_id`, `comment`) VALUES (%(name)s,%(lc)s,%(la)s, %(ba)s,%(cm)s);"
        
        new_survey = mysql.query_db(query, data)
        for sr in request.form.getlist('source'):
            data={
                "survey_id": new_survey,
                "sr_id":sr
            }
            mysql = connectToMySQL('user_survey')
            query = " INSERT INTO  survey_source(`survey_id`, `source_id`) VALUES(%(survey_id)s, %(sr_id)s);"
            sr_servey = mysql.query_db(query,data)
        path = '/results/'+str(new_survey)
        return redirect(path)

#show final result
@app.route('/results/<survey_id>')
def show_one_result(survey_id):
    mysql = connectToMySQL('user_survey')
    query = "SELECT * FROM survey WHERE survey_id = " + survey_id+";"
    survey = mysql.query_db(query)
    name = survey[0]['username']
    comment = survey[0]['comment']
    print("name is ", name)

    mysql = connectToMySQL('user_survey')
    query = "SELECT * FROM location WHERE id = " + str(survey[0]['location_id'])+";"
    print(query)
    lo = mysql.query_db(query)
    print ("lo is",lo)
    location = lo[0]['city'] +','+lo[0]['state']
    print(location)

    mysql = connectToMySQL('user_survey')
    query = "SELECT * FROM language WHERE id = " + \
        str(survey[0]['language_id'])+";"
    print(query)
    la = mysql.query_db(query)
    print("lo is", lo)
    language = la[0]['language'] 
    print("language is",language)

    mysql = connectToMySQL('user_survey')
    query = "SELECT * FROM backgroud WHERE id = " + \
        str(survey[0]['background_id'])+";"
    print(query)
    ba = mysql.query_db(query)
    print("ba is", ba)
    background = ba[0]['backgroud']
    print("bacground is ",background)

    mysql = connectToMySQL('user_survey')
    query = "SELECT  source.source from source inner join survey_source on source.id = survey_source.source_id where survey_source.survey_id =" + \
        survey_id +";"
    print(query)
    s_source = mysql.query_db(query)
    
    print("s_source is ", s_source)

    # return render_template('results.html')
    return render_template('results.html', name=name, location=location, language=language, background=background, source=s_source, comment=comment)

    # # name_from_form = request.form['name']
    # # location_from_form = request.form['location']
    # # language_from_form = request.form['languge']
    # # background_from_form = request.form['background']
    # # s_source = request.form.getlist('source')
    # # print(s_source)
    # # comment_from_form = request.form.get('comments')
    # # print(comment_from_form)
    #     print("data=",data)

    # return render_template('results.html',data=data)
@app.route('/refresh',methods=['POST'])
def refresh():
    return redirect('/')
if __name__=="__main__":
    app.run(debug = True)

