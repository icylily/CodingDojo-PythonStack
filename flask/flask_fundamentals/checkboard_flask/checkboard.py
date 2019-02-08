from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def checkboard():
    # notice the 2 new named arguments!
    return render_template("index.html", x_length = 8, y_length = 8 , color1 = 'blue', color2 = 'red')


@app.route('/<int:x>')
def checkboard_x(x):
    
    return render_template("index.html", x_length=x, y_length=x, color1='blue', color2='red')


@app.route('/<int:x>/<int:y>')
def checkboard_x_y(x,y):
    return render_template("index.html", x_length=x, y_length=y, color1='blue', color2='red')


@app.route('/<int:x>/<int:y>/<string:mycolor1>')
def checkboard_x_y_color1(x, y,mycolor1):
    return render_template("index.html", x_length=x, y_length=y, color1=mycolor1, color2='red')

@app.route('/<int:x>/<int:y>/<string:mycolor1>/<string:mycolor2>')
def checkboard_x_y_color1_color2(x, y,mycolor1,mycolor2):
    return render_template("index.html", x_length=x, y_length=y, color1=mycolor1, color2=mycolor2)

if __name__ == "__main__":
    app.run(debug=True)
