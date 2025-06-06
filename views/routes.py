from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user


main = Blueprint('main', __name__)
@main.route('/')
def home():
    return render_template('home/index.html')