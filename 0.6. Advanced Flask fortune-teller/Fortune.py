from flask import Flask

app = Flask(__name__)




@app.route('/home')
def home():
    return ('<html><p>Home Page</p></html>')









if __name__ == '__main__':
    app.run(debug=True)