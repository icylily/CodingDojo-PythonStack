from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route("/")
def index():
    return render_template("index.html", name="World")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["Name"]
    return redirect("/" + name)


@app.route("/<random>")
def named(random):
    return render_template("index.html", name = random)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.