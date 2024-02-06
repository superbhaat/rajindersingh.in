from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template("front/index.html")
    #return "<p>Hello, Front View!</p>"
