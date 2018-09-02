from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

#directs the site to the home page
@app.route("/")
def home():
    return redirect('/home')

#does the checking for the password and userinfo
def valid_length(userinfo):
    if len(userinfo) > 20 or len(userinfo) < 3:
        return False
    return True

def valid_content(userinfo):
    if ' ' in userinfo:
        return False
    return True

@app.route("/home")
def display_home():
    return render_template('home.html')

@app.route("/home", methods=['POST'])
def validate_usersignup():
# pulls username then checks if it's valid 
    username = request.form['username']

    username_error = ''

    if not valid_length(username):
        username_error = 'Username length must be between 3 and 20 characters'
        username = ''
    elif not valid_content(username):
        username_error = 'Username cannot contain any spaces'
        username = ''

# setting up password/verification, checking if valid
# start with verify password, otherwise if there's an error with the password
# the password is wiped and the verify password won't match, and also have an error
    password = request.form['password']
    verify_password = request.form['verify_password']

    password_error = ''
    verify_password_error = ''

    if password != verify_password:
        verify_password_error = 'Passwords do not match'
        verify_password = ''

    if not valid_length(password):
        password_error = 'Password length must be between 3 and 20 characters'
        password = ''
    elif not valid_content(password):
        password_error = 'Password cannot contain any spaces'
        password = ''
    
# email verification, allows there to be no email, but checks it if there is one
    email = request.form['email']
    email_error = ''

    if email:
        if '@' not in email or '.' not in email:
            email_error = "Not a valid e-mail address"
            email = ''

# if there are no errors, it redirects the user to the welcome site with the username
    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))

# if there are errors, the home page stays up, displays the errors, keeps the email and username 
# but not the passwords
    else:
        return render_template('home.html',
            username_error = username_error,
            password_error = password_error,
            verify_password_error = verify_password_error,
            email_error = email_error,
            username = username,
            email = email
            )

@app.route('/welcome')
def welcome():
    name = request.args.get('username')
    return render_template('welcome.html', username = name)

app.run()