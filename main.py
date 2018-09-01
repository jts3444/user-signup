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

def valid_length(userinfo):
    if len(userinfo) > 20 or len(userinfo) < 3:
        return False
    return True

def valid_content(userinfo):
    if ' ' in userinfo:
        return False
    return True

def validate_usersignup():
# checking username   
    username = request.form['username']

    username_error = ''

    if valid_length(username) == False:
        username_error = 'Username length must be between 3 and 20 characters'
        username = ''
    elif valid_content(username) == False:
        username_error = 'Username cannot contain any spaces'
        username = ''

# setting up password, checking if valid
    password = request.form['password']

    password_error = ''

    if len(password) > 20 or len(password) < 3:
        password_error = 'Password length must be between 3 and 20 characters'
        password = ''
    elif ' ' in password:
        password_error = 'Password cannot contain any spaces'
        password = ''

# checking verify password input
    verify_password = request.form['verify_password']

    verify_password_error = ''

    if password != verify_password:
        verify_password_error = 'Passwords do not match'
        verify_password = ''

# email verification
    email = request.form['email']
    email_error = ''

    if email == True:
        if ['@', '.'] not in email:
            email_error = "Not a valid e-mail address"
            email = ''

    if not username_error and not password_error and not verify_password_error and not email_error:
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