from flask import Flask, render_template, request, make_response
from mysql import connector

cnx = connector.connect()

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/about")
def About():
    return render_template("About Us.html")

@app.route("/destination")
def Destination():
    return render_template("Destinations.html")

@app.route("/book")
def Book():
    return render_template("Book Now.html")

@app.route("/login")
def Login():
    return render_template("Login.html")

@app.route("/packages")
def Packages():
    return render_template("Packages.html")

@app.route("/registration")
def Registration():
    return render_template("Registration.html")

@app.route("/login_process", methods=["POST"])
def Login_Process():
    data = request.form
    username = data["username"]
    password = data["password"]
    cursor = cnx.cursor()
    cursor.execute("", {username: username, password: password})
    cnx.commit()
    return make_response([username, password], 200)

@app.route("/book_process", methods=["post"])
def Book_process():
    data = request.form
    fullname = data["fullname"]
    
@app.route("/registration_process", methods=["post"])
def Registration_process():
    data = request.form
    fullname=data["fullname"]
    