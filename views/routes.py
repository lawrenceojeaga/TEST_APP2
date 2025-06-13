from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user


main = Blueprint('main', __name__)
@main.route('/')
def home():
    return render_template('home/index.html')

@main.route('/view_items')
@login_required
def view_items():
    items = [
        {
            'id': 1,
            'name': 'Classic Sneakers',
            'description': 'Comfortable sneakers for everyday wear.',
            'price': 59.99,
            'image': 'images/sneakers.jpg'
        },
        {
            'id': 2,
            'name': 'Stylish Backpack',
            'description': 'Perfect backpack for school or travel.',
            'price': 79.99,
            'image': 'images/backpack.jpg'
        },
        {
            'id': 3,
            'name': 'Smart Watch',
            'description': 'Track your health and notifications.',
            'price': 149.99,
            'image': 'images/watch.jpg'
        }
    ]
    return render_template('items/view_items.html', items=items)

