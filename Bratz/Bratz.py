from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

firebaseConfig = {
    'apiKey': "AIzaSyDIADdWgwg8cxTfrD2gnY2_OT6uwuMlla4",
    'authDomain': "bratz-project.firebaseapp.com",
    'projectId': "bratz-project",
    'storageBucket': "bratz-project.appspot.com",
    'messagingSenderId': "380577286146",
    'appId': "1:380577286146:web:34495df793b371dfc6ff1b",
    'measurementId': "G-2KK04QH44S",
    "databaseURL": "https://bratz-project-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['full_name']
        username = request.form['username']
        
        try:
            user = auth.create_user_with_email_and_password(email, password)
            uid = user['localId']
            
            db.child("Users").child(uid).set({"full_name": full_name, "email": email, "username": username})

            session['user'] = uid
            session['user_email'] = email

            return redirect(url_for('quiz'))

        except Exception as e:
            error = str(e)
            return render_template("signup.html", error=error)

    return render_template("signup.html")

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            uid = user['localId']
            
            session['user'] = uid
            session['user_email'] = email

            return redirect(url_for('quiz'))

        except Exception as e:
            error = str(e)
            return render_template("signin.html", error=error)

    return render_template("signin.html")

@app.route('/signout')
def signout():
    session.pop('user', None)
    session.pop('user_email', None)
    return redirect(url_for('home'))

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if 'user' not in session: 
        return redirect(url_for('home'))
    questions = [
        {"question": "What's your favorite color?", "options": ["Pink", "Blue", "Green", "Purple"]},
        {"question": "What's your favorite activity?", "options": ["Shopping", "Dancing", "Sports", "Reading"]},
        {"question": "What's your favorite accessory?", "options": ["Hat", "Sunglasses", "Scarf", "Jewelry"]},
        {"question": "What's your favorite type of music?", "options": ["Pop", "Rock", "Classical", "Hip-hop"]},
    ]

    


    if request.method == 'POST':
        answer1 = request.form['0']
        answer2 = request.form['1']
        answer3 = request.form['2']
        answer4 = request.form['3']
        answers=[answer1,answer2,answer3,answer4]
        db.child("answers").push(answers)
        
        counts = {
            "Cloe": 0,
            "Sasha": 0,
            "Jade": 0,
            "Yasmin": 0
        }

        for answer in answers:
            if answer == "Pink":
                counts["Cloe"] += 1

            elif answer == "Blue":
                counts["Sasha"] += 1
            elif answer == "Green":
                counts["Jade"] += 1
            elif answer == "Purple":
                counts["Yasmin"] += 1

        character = max(counts, key=counts.get)
        

        db.child("characters").push(character)

        return render_template("quiz_results.html", character=character)

    return render_template("quiz.html", questions=questions)

@app.route('/stories')
def stories():
    if 'user' not in session: 
        return redirect(url_for('home'))
    return render_template("stories.html")



if __name__ == '__main__':
    app.run(debug=True,port=50011)
