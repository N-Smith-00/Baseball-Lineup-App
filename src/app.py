from flask import Flask, redirect, render_template, request
from main import App

app = Flask(__name__)

@app.before_request
def load_data():
    # load data if it exists, else create app class
    pass

@app.route('/')
def index():
    return redirect('/home', code=302)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login_post():
    username = request.form['username'].lower()
    password = request.form['password']
    return redirect('/profile', code=302)

@app.route('/create-team')
def create_team():
    return render_template('createTeam.html')

@app.route('/create-player')
def create_player():
    return render_template('createPlayer.html')

if __name__ == "__main__":
    app.run()
    driver = App()