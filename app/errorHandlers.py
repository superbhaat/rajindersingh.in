from app import app
from flask import render_template, redirect

@app.errorhandler(404)
def errorhandler(e):
    print(e)
    return render_template("404.html")