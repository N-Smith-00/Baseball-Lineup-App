from flask import Flask, redirect, render_template
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

@app.route('/create-team')
def create_team():
    return render_template('createTeam.html')

@app.route('/create-player')
def create_player():
    return render_template('createPlayer.html')