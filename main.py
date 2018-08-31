from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

'''@app.route("/")
def home():
    return render_template('home.html')
'''
@app.route("/home")
def display_home():
    return render_template('home.html')

@app.route("/home", methods=['POST'])
def validate_usersignup():
    username = request.form['username']

    username_error = ''

    if len(username) > 20 or len(username) < 3:
        username_error = 'Username length must be between 3 and 20 characters'
        username = ''
    elif ' ' in username:
        username_error = 'Username cannot contain any spaces'
        username = ''

    password = request.form['password']

    password_error = ''

    if len(password) > 20 or len(password) < 3:
        password_error = 'Password length must be between 3 and 20 characters'
        password = ''
    elif ' ' in password:
        password_error = 'Password cannot contain any spaces'
        password = ''

    password = request.form['password']
    verify_password = request.form['verify_password']

    verify_password_error = ''

    if password != verify_password:
        verify_password_error = 'Passwords do not match'
        verify_password = ''

    email = request.form['email']

    if not username_error and not password_error and not verify_password_error:
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('home.html',
            username_error = username_error,
            password_error = password_error,
            verify_password_error = verify_password_error,
            username = username,
            email = email
            )


@app.route('/welcome')
def welcome():
    name = request.args.get('username')
    return render_template('welcome.html', username = name)

app.run()