from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

def validate_email(email):
    errors = []
    at_count = 0
    dot_count = 0

    if email == "":
        return errors

    for character in email:
        if character == "@":
            at_count += 1
        if character == ".":
            dot_count += 1

    if at_count == 0:
        errors.append('Email must have an "@" symbol.')

    if dot_count == 0:
        errors.append('Email must have a "." symbol.')

    if at_count >= 2:
        errors.append('Email can only have one "@" symbol.')

    if dot_count >= 2:
        errors.append('Email can only have one "." symbol.')

    if ' ' in email:
        errors.append('Email cannot have spaces. ')

    if len(email) < 3:
        errors.append('Email must have at least 3 characters. ')

    if len(email) > 20:
        errors.append('Email cannot have more than 20 chracters. ')

    return errors

@app.route("/", methods=['GET'])
def display():
    input_errors = {'username':[]}
    return render_template('home.html', input_errors=input_errors)

@app.route("/", methods=['POST'])
def form_data():
    py_username = request.form['username']
    py_password = request.form['password']
    py_password2 = request.form['password2']
    py_email = request.form['email']
    input_errors = {'username':[], 'password':[], 'password2':[], 'email':[]}

    if py_username == "":
        input_errors['username'].append('Input cannot be blank. ')

    for letter in py_username:
        if letter == ' ':
            input_errors['username'].append('Input cannot have spaces. ')
            break

    if len(py_username) < 3:
        input_errors['username'].append('Username must have at least 3 characters. ')

    if len(py_username) > 20:
        input_errors['username'].append('Username cannot have more than 20 chracters. ')

    #--
    if py_password == "":
        input_errors['password'].append('Input cannot be blank. ')

    for letter in py_password:
        if letter == ' ':
            input_errors['password'].append('Input cannot have spaces. ')
            break

    if len(py_password) < 3:
        input_errors['password'].append('Password must have at least 3 characters. ')

    if len(py_password) > 20:
        input_errors['password'].append('Password cannot have more than 20 chracters. ')

    #--
    if py_password2 != py_password:
        input_errors['password2'].append('Must match original password entry. ')

    #--
    input_errors['email'] = validate_email(py_email)

    if input_errors == {'username':[], 'password':[], 'password2':[], 'email':[]}:
        return render_template('welcome.html', html_username=py_username)

    return render_template('home.html', input_errors=input_errors, html_username=py_username, html_password=py_password, html_password2=py_password2, html_email=py_email)

app.run()
