from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello There</h1>'

@app.route('/home', methods=['GET', 'POST'])
def home():
    links = [{ "url" : "https://www.google.com", "text": "Google" }, { "url" : "https://www.facebook.com", "text": "Facebook" }, { "url" : "https://www.udemy.com", "text": "Udemy" }]
    return render_template('template.html', my_var="Liv", links=links) 

# @app.route('/home/<place>')
# def home(place):
#     return '<h1>Welcome to ' + place + ' page</h1>'

if __name__ == '__main__':
    app.run(debug=True)