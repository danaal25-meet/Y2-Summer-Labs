from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = "super-secret-key"

firebaseConfig = {
  "apiKey": "AIzaSyCbgHgrptDTjD9Mh1Pf_U8zBkMUIk_QK-8",
  "authDomain": "labbb-2e171.firebaseapp.com",
  "projectId": "labbb-2e171",
  "storageBucket": "labbb-2e171.appspot.com",
  "messagingSenderId": "1061000358749",
  "appId": "1:1061000358749:web:9e25196a54b6b80c2f16b4",
  "measurementId": "G-MBJPYJ6EMP",
  "databaseURL":"https://labbb-2e171-default-rtdb.europe-west1.firebasedatabase.app//"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:  
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        full_name = request.form['full_name']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            user_id = user['localId']
            db.child("users").child(user_id).set({
                "full_name": full_name,
                "email": email,
                "username": username
            })
            login_session['user'] = user
            return redirect(url_for('home'))
        except Exception as e:
            error = e
            return render_template("signup.html", error=error)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template("signin.html")
    else:  
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            if 'quotes' not in login_session:
                return redirect(url_for('home'))
        except:
            error = "Sign in failed. Try again."
            return render_template("signin.html", error=error)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if login_session['user'] == None:
        return redirect(url_for('signup'))
    if request.method == "GET":
        return render_template("home.html")
    elif request.form['action'] =='signout':
        login_session['user'] = None
        auth.current_user = None
        return redirect(url_for('signin'))
    else:
        qoute = {"text":request.form['quote'],"said_by":request.form['speaker'],"uid":login_session['user']['localId']}
        db.child("Qoutes").push(qoute)
        return redirect(url_for('thanks'))

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")

@app.route('/display')
def display():
    Qoutes=db.child("Qoutes").get().val()
    return render_template("display.html",qoutes=Qoutes)

@app.route('/signout')
def signout():
    login_session.pop('user', None)
    login_session.pop('quotes', None)
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True,port= 5001)
