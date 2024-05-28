import os
import psycopg2
from flask import Flask,render_template, request, session, redirect, url_for
import re
app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='poetry_db',
                            user="postgres",
                            password="KOV125456")
    return conn
conn = get_db_connection()
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route("/")
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM accounts WHERE username = '{username}' AND password = '{password}';")
        account = cur.fetchone()
        if account:
            session['loggedin'] = True
            session['username'] = account[1]
            msg = 'Logged in successfully !'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM accounts WHERE username = '{username}';")
        account = cur.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cur.execute(f"INSERT INTO accounts VALUES (DEFAULT, '{username}', '{password}', '{email}');")
            msg = 'You have successfully registered !'
            conn.commit()
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

if __name__ == '__main__':
    app.run()
