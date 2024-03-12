from flask import Blueprint, render_template, request, redirect, url_for, flash
from DB import mongo

register_blueprint = Blueprint('register', __name__)

@register_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        contact = request.form['contact']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if username already exists
        existing_user = mongo.db.users.find_one({'email': email})
        if existing_user:
            flash('Username already exists. Please choose another one.', 'error')
            return redirect(url_for('register.register'))

        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'error')
            return redirect(url_for('register.register'))

        # Insert new user into the database
        new_user = {
            'name': name,
            'address': address,
            'contact': contact,
            'email': email,
            'password': password  # You should hash the password for security
        }
        mongo.db.users.insert_one(new_user)
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login.login'))

    return render_template('register.html')
