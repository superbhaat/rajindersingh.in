from app import app

from flask import render_template, request, redirect

@app.route("/")
def index():
    return render_template("front/index.html")
    #return "<p>Hello, Front View!</p>"

@app.route("/getInTuch",  methods=["GET", "POST"])
def getInTuch():
    if request.method == "POST":
        yourName = request.form.get("yourName")
        email = request.form.get("email")
        phoneNumber = request.form.get("phoneNumber")
        message = request.form.get("message")
        print(yourName)
    return render_template("front/index.html")


@app.route("/form",  methods=["GET", "POST"])
def form():
    return render_template("front/form.html")