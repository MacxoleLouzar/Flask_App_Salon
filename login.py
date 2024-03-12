from flask import Blueprint, render_template, request, redirect, url_for, flash
from DB import mongo

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the email and password match
        user = mongo.db.users.find_one({'email': email, 'password': password})  # You should hash the password for security
        if user:
            # If the user exists, set a session variable to indicate they are logged in
            # Here, you might also want to redirect to a dashboard or profile page
            flash('Login successful!', 'success')
            return redirect(url_for('landing'))

        flash('Invalid email or password. Please try again.', 'error')
        return redirect(url_for('login.login'))

    return render_template('login.html')
