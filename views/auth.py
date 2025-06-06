from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Here you would typically check the username and password against your user database
        # For demonstration, we assume a user with username 'user' and password 'password'
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            return render_template('auth/login.html', error='Invalid credentials no such user found !')
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Here you would typically save the new user to your user database
        # For demonstration, we assume a simple in-memory storage
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        
        # Save the new user to the database (this is just a placeholder)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')