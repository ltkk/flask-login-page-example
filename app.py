"""
    Created by nguyenvanhieu.vn at 9/16/2018
"""
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return redirect('/login')


@app.route('/home')
def home():
    return 'Login success!'


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
