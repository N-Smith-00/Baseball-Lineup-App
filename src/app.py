from flask import Flask, redirect, render_template

app = Flask(import_name="Lineup App")

@app.route('/')
def index():
    return redirect("/home", code=302)

@app.route("/home")
def home():
    return "this is the home page"