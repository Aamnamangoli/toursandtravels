from flask import Flask, render_template, request, make_response, session
from mysql import connector

cnx = connector.connect(
    host='127.0.0.1',
    port='3306',
    user='WL',
    password='123',
    database="WonderLust"
)

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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
    if(session["id"] < 1):
        return make_response("", 403)
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

@app.route("/logout")
def logout():
    session.clear()
    return make_response("", 200)

@app.route("/registration_process", methods=["POST"])
def Registration_process():
    data = request.form
    name = data["fullname"]
    email = data ["email"]
    password = data ["password"]
    confirm_password = data ["confirm-password"]
    
    try:        
        cursor = cnx.cursor()
        sql = "INSERT INTO USERS(FULLNAME, EMAIL, PASSWORD) VALUES(%(fullname)s, %(email)s, %(password)s);"
        values = {"fullname": name, "email": email, "password": password}
            
        cursor.execute(sql, values)
        cnx.commit()
            
        cursor.close()
    
    except connector.Error as e:
        print(e)
    except:
        print("Error")
        
    return make_response([name, email, password, confirm_password], 200)
    
@app.route("/login_process", methods=["POST"])
def Login_Process():
    data = request.form
    email = data["email"]
    password = data["password"]
    id = -1
    try:
        cursor = cnx.cursor()
        sql = "SELECT ID FROM USERS WHERE EMAIL=%(email)s AND PASSWORD=%(password)s;"
        values = {"email": email, "password": password}
                
        cursor.execute(sql, values)
        for i in cursor.fetchone():
            id = i
        
        cursor.close()
        cnx.commit()
    except connector.Error as e:
        print(e)
    except:
        print("Error")
    
    session["id"] = id
    return make_response([email, password], 200)

@app.route("/book_process", methods=["post"])
def Book_process():
    if(session["id"] < 1):
        return make_response("", 403)
    
    id = session["id"]
    data = request.form
    fullname = data["fullname"]
    email = data["email"]
    phone = data["phone"]
    destination = data["dest"]
    date = data["date"]
    number = data["number"]
    
    try:        
        cursor = cnx.cursor()
        sql = "INSERT INTO BOOK(USER_ID, FULLNAME, EMAIL, PHONE, DESTINATION, TRAVEL_DATE, NUM_OF_TRAVELERS) VALUES(%(id)s, %(fullname)s, %(email)s, %(phone)s, %(destination)s, %(date)s, %(number)s);"
        values = {"id": id, "fullname": fullname, "email": email, "phone": phone, "destination": destination, "date": date, "number": number}
            
        cursor.execute(sql, values)
        cursor.close()
        cnx.commit()
        
    except connector.Error as e:
        print(e)
    except:
        print("Error")
        
    return make_response([fullname,email,phone,date,number], 200)

@app.route("/book_retrieve", methods=["GET"])
def GET_Booking():
    if(session["id"] < 1):
        return make_response("", 403)
    
    id = session["id"]
    try:        
        cursor = cnx.cursor()
        sql = "SELECT * FROM BOOK WHERE USER_ID=%(id)s;"
        values = {"id": id}
            
        cursor.execute(sql, values)
        
        result = cursor.fetchall()
        
        cursor.close()
        cnx.commit()
        
    except connector.Error as e:
        print(e)
    except:
        print("Error")
        
    return make_response("", 200)

@app.route("/book_delete", methods=["DELETE"])
def Delete_Booking():
    if(session["id"] < 1):
        return make_response("", 403)
    
    user_id = session["id"]
    data = request.form
    id = data["id"]
    
    try:        
        cursor = cnx.cursor()
        sql = "DELETE FROM BOOK WHERE USER_ID=%(user_id)s AND ID=%(id)s;"
        values = {"user_id": user_id,"id": id}
            
        cursor.execute(sql, values)
        cursor.close()
        cnx.commit()
        
    except connector.Error as e:
        print(e)
    except:
        print("Error")
        
    return make_response("",200)