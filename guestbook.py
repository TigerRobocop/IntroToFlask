from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql10243121:jEbSnYMlax@sql10.freemysqlhosting.net/sql10243121'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20))
    content = db.Column(db.String(1000))

@app.route('/')
def index():
    results = Comments.query.all()

    return render_template('index.html', results = results)

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    content = request.form['content']

    signature = Comments(author = author, content = content)
    db.session.add(signature)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/home', methods=['GET', 'POST'])
def home():
    links = [{ "url" : "https://www.google.com", "text": "Google" }, { "url" : "https://www.facebook.com", "text": "Facebook" }, { "url" : "https://www.udemy.com", "text": "Udemy" }]
    return render_template('template.html', my_var="Liv", links=links) 

if __name__ == '__main__':
    app.run(debug=True)