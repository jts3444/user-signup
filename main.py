from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/home')
def display_home():
    return render_template('home.html')

def validate_username():
    username = request.form['username']

    username_error = ''

    if len(username) > 20 or len(username) < 3:
            username_error = 'Username length must be between 3 and 20 characters'
            username = ''

@app.route('/welcome')
def welcome():
    username = request.form['username']
    return render_template('welcome.html')

app.run()