from flask import Flask

app = Flask(__name__)

@app.route('/food1')
def food1 ():
    return('''<html> 
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMD1OIk-O-1r6sRwwUS2r6vfnR2UuQSqpUwA&s">
            <a href='food2!'>Go to food 2> 

        </html>''')

@app.route('/food2')
def food2():
    return('''<html> 
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxdoJUwzsh126JZH0qSdMA55OQHiZKAqx6Hw&s">


        </html>''')

@app.route('/food3')
def food3 ():
    return('''<html> 
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvC1pGhW7_BRwnGuBguLE99tfA0faYflekCA&s">
        <a href='home'>Go to the main page>

        </html>''')



@app.route('/home')
def home():
    return('''<html>
        <h1> Heading</h1>
        <p>Welcome to my webpage!!</p>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMD1OIk-O-1r6sRwwUS2r6vfnR2UuQSqpUwA&s">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE8rlBbqnDycGlg4HYo7CnnMOdSE7JA6ICkg&s">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSArtNvfXmXPL3m2NUPQYsze8TP_rJpeYMTxA&s">
        <div>
        <a href='/food1'>Go to the food page
        <div>
        <a href='/space2'>Go to the space page
        <div>
        <a href='/pet1'>Go to the pet page
        

     </html>''')

    
@app.route('/pet1')
def pet1 ():
    return('''<html> 
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSArtNvfXmXPL3m2NUPQYsze8TP_rJpeYMTxA&s">
        <div>
        <a href='pet1'>Go to pet 1>
        <div>
        <a href='pet3'>Go to pet 3>
        </html>''')




@app.route('/pet2')
def pet2 ():
    return('''<html> 
        <img src="https://www.humanesociety.org/sites/default/files/styles/768x326/public/2020-07/dog-509745.jpg?h=e22bf01e&itok=MGmnQnfa">
        
        </html>''')


@app.route('/pet3')
def pet3 ():
    return('''<html> 
        <img src"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGVG6MMCMIRITukWBdFmO_EFgdVyL78focaw&s">



        </html>''')






@app.route('/space1')
def space1 ():
    return('''<html> 
        <img src="data:image/jpeg;base64,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" alt="alternatetext">
        <a href='space3'>Go to space 3>
        </html>''')

@app.route('/space2')
def space2 ():
    return('''<html> 
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE8rlBbqnDycGlg4HYo7CnnMOdSE7JA6ICkg&s">
        <a href='space1'>Go to space 1>
        </html>''')

@app.route('/space3')
def space3 ():
    return('''<html> 
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_0rI1nJsBh43LVrAi6e4XR4tQShnR3wsRnA&s">








if __name__ == '__main__':
    app.run(debug=True) 