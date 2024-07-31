from flask import Flask , render_template, request, url_for, redirect
import random

app = Flask(__name__)

fortunes = [
        "You will have a great day!",
        "Something unexpected will happen today.",
        "You will achieve your goals.",
        "Happiness is coming your way.",
        "Be cautious of new opportunities.",
        "A new friendship will bring joy to your life.",
        "You will find success in your career.",
        "Love is around the corner.",
        "A pleasant surprise is waiting for you.",
        "Your hard work will soon pay off."
    ]




@app.route('/home')
def home():
    return render_template("home.html")

# @app.route('/fortune')
# def fortune():
#     selected_fortune = random.choice(fortunes)
#     return render_template('fortune.html', fortune=selected_fortune)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['tt']
        return redirect(url_for('fortune', n=name))
    return render_template("home")
return render_template("login.html")

@app.route("/home")
def home():
    if 'name' not in session:
        return redirect(url_for(login))
    name = session['name']
    return render_template("home.html", name=name)

@app.route('/fortune')
def fortune():
    if 'name' not in session:s
        return redirect(url_for('login'))

@app.route('/fortune')
def fortune(n):
    if len(n) < 10:
        random_fortune = fortunes[len(n)]
    else:
        random_fortune = random.choice(fortunes)
    return render_template("fortune.html", name=n, fortune=random_fortune)



if __name__ == '__main__':
    app.run(debug = True,port = 5003)
