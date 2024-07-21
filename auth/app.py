from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = "super-secret-key"

firebaseConfig = {
  "apiKey": "AIzaSyC5LJTPAhVruC63STy7zOboBEP722vVilY",
  "authDomain": "authenticationfacebook-62c9c.firebaseapp.com",
  "projectId": "authenticationfacebook-62c9c",
  "storageBucket": "authenticationfacebook-62c9c.appspot.com",
  "messagingSenderId": "372646840186",
  "appId": "1:372646840186:web:294cc7d04536f3a7e338c3",
  "measurementId": "G-G35T7N123P",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:  
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            login_session['quotes'] = []
            return redirect(url_for('home'))
        except:
            error = "Signup failed. Try again."
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
                login_session['quotes'] = []
            return redirect(url_for('home'))
        except:
            error = "Sign in failed. Try again."
            return render_template("signin.html", error=error)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        quote = request.form['quote']
        login_session['quotes'].append(quote)
        return redirect(url_for('thanks'))

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")

@app.route('/display')
def display():
    quotes = login_session.get('quotes', [])
    return render_template('display.html', quotes=quotes)

@app.route('/signout')
def signout():
    login_session.pop('user', None)
    login_session.pop('quotes', None)
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
