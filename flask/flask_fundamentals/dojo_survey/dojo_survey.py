from flask import Flask,render_template,redirect,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results',methods= ['GET', 'POST'])
def show_results():
    print("Got Post Info")
    # print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['languge']
    background_from_form = request.form['background']
    s_source = request.form.getlist('source')
    print(s_source)
    comment_from_form = request.form.get('comments')
    print(comment_from_form)

    return render_template('results.html', name=name_from_form, location=location_from_form, language=language_from_form, background=background_from_form, source=s_source, comment=comment_from_form)
@app.route('/refresh',methods=['POST'])
def refresh():
    return redirect('/')
if __name__=="__main__":
    app.run(debug = True)

