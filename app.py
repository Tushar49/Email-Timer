from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
import json
import re
import time

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your_secret_key'
Session(app)

users = []

def email_exists(email_timers, email):
    return any(timer['email'] == email for timer in email_timers)

def get_user_by_email(email):
    for user in users:
        if user['email'] == email:
            return user
    return None

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if get_user_by_email(email) is not None:
            flash('Email already exists. Please log in or use another email.', 'error')
            return redirect(url_for('signup'))

        hashed_password = generate_password_hash(password)
        new_user = {'email': email, 'password': hashed_password}
        users.append(new_user)
        flash('Account created successfully. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = get_user_by_email(email)

        if user is None or not check_password_hash(user['password'], password):
            flash('Invalid email or password. Please try again.', 'error')
            return redirect(url_for('login'))

        session['user_email'] = email
        flash('Logged in successfully.', 'success')
        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_email', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user_email' not in session:
        return redirect(url_for('login'))

    email_timers = session.get('email_timers', [])

    if request.method == 'POST':
        email_input = request.form['email']
        emails = re.split(r'[,;\s]\s*', email_input.strip())

        for email in emails:
            if not email_exists(email_timers, email):
                email_timers.append({'email': email, 'status': 'Ready', 'end_time': 0})

        session['email_timers'] = email_timers

    return render_template('index.html', email_timers=email_timers)

@app.route('/start_timer/<int:email_timer_index>')
def start_timer(email_timer_index):
    if 'user_email' not in session:
        return redirect(url_for('login'))

    email_timers = session['email_timers']
    email_timer = email_timers[email_timer_index]
    email_timer['status'] = 'InUse'
    email_timer['end_time'] = int(time.time()) + 60
    session['email_timers'] = email_timers

    return redirect(url_for('index'))

@app.route('/delete_timer/<int:email_timer_index>')
def delete_timer(email_timer_index):
    if 'user_email' not in session:
        return redirect(url_for('login'))

    email_timers = session['email_timers']
    del email_timers[email_timer_index]
    session['email_timers'] = email_timers

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
