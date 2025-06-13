from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, db
from sqlalchemy import text

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']

        # Raw SQL vulnerable to injection
        sql = f"SELECT * FROM user WHERE username = '{username}'"
        print(f"Executing SQL: {sql}")
        result = db.session.execute(text(sql)).fetchone()

        if result:
            # Find the actual user object using the ID or username
            user = User.query.filter_by(id=result.id).first()
            if user:
                login_user(user)  # 👈 This tells Flask-Login the user is authenticated
                return redirect(url_for('main.view_items'))

        flash('Invalid login', 'login')
    
    return render_template('auth/login.html')

# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         # Here you would typically check the username and password against your user database
#         # For demonstration, we assume a user with username 'user' and password 'password'
#         user = User.query.filter_by(username=username).first()
#         if user and check_password_hash(user.password, password):
#             login_user(user)
#             return redirect(url_for('main.home'))
#         else:
#             return render_template('auth/login.html', error='Invalid credentials no such user found !')
#     return render_template('auth/login.html')

# Creating a new route for users

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Here you would typically save the new user to your user database
        # For demonstration, we assume a simple in-memory storage
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)
        
        # Save the new user to the database (this is just a placeholder)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

# Creating a new route for logout

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))