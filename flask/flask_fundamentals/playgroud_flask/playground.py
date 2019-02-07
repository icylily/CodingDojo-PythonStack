from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def three_playgrounds():
    # notice the 2 new named arguments!
    return render_template("index.html", amounts=3)


@app.route('/play/<int:myamounts>/<string:mycolor>')
def multi_colored_playgrounds(myamounts, mycolor):
    print(mycolor)
    print(myamounts)
    return render_template("index.html", amounts=myamounts, color=mycolor)

@app.route('/play/<int:myamounts>')
def multi_playgrounds(myamounts):
    
    return render_template("index.html", amounts=myamounts)
   



if __name__ == "__main__":
    app.run(debug=True)
