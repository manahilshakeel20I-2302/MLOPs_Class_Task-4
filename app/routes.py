from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User, db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            flash('Email already exists!', 'error')
        else:
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
        return redirect(url_for('main.home'))
    
    return render_template('submit.html')
