from app import app

from flask import render_template

@app.route("/admin")
def adminIndex():
    return render_template("admin/index.html")
    #return "<p>Hello, Admin View!</p>"