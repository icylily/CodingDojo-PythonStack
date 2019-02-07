from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return"hello,world."


@app.route('/dojo')
def dojo():
    return"dojo."


@app.route('/say/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hi %s' % username



@app.route('/repeat/<int:times>/<string:text>')
def show_text(times,text):
    # show the user profile for that user
    return '%s \n\r' % text *int(times)



if __name__=="__main__":
    app.run(debug=True)
